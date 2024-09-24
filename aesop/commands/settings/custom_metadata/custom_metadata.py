from typing import List

import typer
from rich import print

from aesop.commands.common.exception_handler import exception_handler
from aesop.config import AesopConfig
from aesop.console import console
from aesop.graphql.generated import client
from aesop.graphql.generated.input_types import CustomMetadataConfigInput, SettingsInput

app = typer.Typer(help="Custom metadata settings")


@app.command()
def get(
    ctx: typer.Context,
) -> None:
    config: AesopConfig = ctx.obj
    client = config.get_graphql_client()
    settings = client.get_custom_metadata_settings()
    custom_metadata_configs = settings.settings.custom_metadata_config
    if not custom_metadata_configs:
        raise ValueError  # Impossible!
    print([cfg.model_dump() for cfg in custom_metadata_configs])


@exception_handler("Add custom metadata")
def _validate_custom_metadata_config(
    value: str,
) -> str:
    CustomMetadataConfigInput.model_validate_json(value)
    return value


def _get_existing_configs(
    client: client.Client,
) -> List[CustomMetadataConfigInput]:
    return [
        CustomMetadataConfigInput.model_validate(cfg.model_dump())
        for cfg in client.get_custom_metadata_settings().settings.custom_metadata_config
        or []
    ]


@app.command()
def add(
    ctx: typer.Context,
    input: str = typer.Argument(
        help="A JSON representing the custom metadata config to add.",
        callback=_validate_custom_metadata_config,
    ),
) -> None:
    config: AesopConfig = ctx.obj
    client = config.get_graphql_client()
    new_config = CustomMetadataConfigInput.model_validate_json(input)
    existing_configs = _get_existing_configs(client)
    client.update_settings(
        input=SettingsInput(customMetadataConfig=[*existing_configs, new_config])
    )
    console.ok("Added custom metadata config")


@app.command(help="Removes all metadata configs associated with a key.")
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
