import csv
import sys
from typing import List

import typer
from pydantic import TypeAdapter
from rich import print, print_json
from rich.table import Column, Table

from aesop.commands.common.arguments import InputFileArg
from aesop.commands.common.enums.output_format import OutputFormat
from aesop.commands.common.exception_handler import exception_handler
from aesop.commands.common.models import InputModel
from aesop.commands.common.options import OutputFormatOption
from aesop.config import AesopConfig
from aesop.console import console
from aesop.graphql.generated import client
from aesop.graphql.generated.enums import CustomMetadataDataType
from aesop.graphql.generated.get_custom_metadata_settings import (
    GetCustomMetadataSettingsSettingsCustomMetadataConfig as Config,
)
from aesop.graphql.generated.input_types import (
    CustomMetadataConfigInput,
    SettingsInput,
    UpdateCustomMetadataConfigInput,
)

app = typer.Typer(help="Custom metadata settings")


def _display(
    configs: List[Config],
    output: OutputFormat,
) -> None:
    if output is OutputFormat.JSON:
        print_json(TypeAdapter(List[Config]).dump_json(configs).decode())
    elif output is OutputFormat.CSV:
        spamwriter = csv.writer(sys.stdout)
        fields = list(Config.model_fields.keys())
        spamwriter.writerow(fields)
        for config in configs:
            spamwriter.writerow([config.model_dump()[x] for x in fields])
    else:
        table = Table(
            Column(header="Key", no_wrap=True, style="bold cyan"),
            "Display Name",
            "Data Type",
            "Highlight",
            "Searchable",
            show_lines=True,
        )
        for config in configs:
            table.add_row(
                config.key,
                config.display_name,
                config.data_type,
                str(config.highlight or False),
                str(config.searchable or False),
            )
        print(table)


@exception_handler("Get custom metadata configs")
@app.command()
def get(ctx: typer.Context, output: OutputFormat = OutputFormatOption) -> None:
    config: AesopConfig = ctx.obj
    client = config.get_graphql_client()
    settings = client.get_custom_metadata_settings()
    custom_metadata_configs = settings.settings.custom_metadata_config
    if not custom_metadata_configs:
        raise ValueError  # Impossible!
    _display(custom_metadata_configs, output)


def _get_existing_configs(
    client: client.Client,
) -> List[CustomMetadataConfigInput]:
    return [
        CustomMetadataConfigInput.model_validate(cfg.model_dump())
        for cfg in client.get_custom_metadata_settings().settings.custom_metadata_config
        or []
    ]


class UpdateConfigInput(UpdateCustomMetadataConfigInput, InputModel):
    @staticmethod
    def example_json(indent: int = 0) -> str:
        example = UpdateCustomMetadataConfigInput(
            dataType=CustomMetadataDataType.OBJECT,
            displayName="A custom metadata config",
            key="md1",
            searchable=True,
            highlight=False,
        )
        return example.model_dump_json(indent=indent)


@exception_handler("Update custom metadata config")
@app.command(
    help="Updates a config for a custom metadata. If no such config exists, "
    "it will be added.",
)
def update(
    ctx: typer.Context,
    input: typer.FileText = InputFileArg(UpdateConfigInput),
) -> None:
    config: AesopConfig = ctx.obj
    res = (
        config.get_graphql_client()
        .update_custom_metadata_config(
            UpdateConfigInput.model_validate_json(input.read())
        )
        .update_custom_metadata_config
    )
    print_json(res.model_dump_json())


@exception_handler("Remove custom metadata config")
@app.command(help="Removes the metadata config associated with a key.")
def remove(
    ctx: typer.Context,
    key: str = typer.Argument(
        help="The key to remove custom metadata configs for.",
    ),
) -> None:
    config: AesopConfig = ctx.obj
    client = config.get_graphql_client()
    existing_configs = _get_existing_configs(client)
    updated_configs = [cfg for cfg in existing_configs if cfg.key != key]
    client.update_settings(
        input=SettingsInput(
            customMetadataConfig=updated_configs,
        )
    )
    removed_config_count = len(existing_configs) - len(updated_configs)
    console.ok(
        f"Removed {removed_config_count} "
        f"custom metadata config{'s' if removed_config_count > 1 else ''}"
    )
