import csv
import json
import sys
from typing import Dict, List

from pydantic import BaseModel, TypeAdapter
from rich import print, print_json
from rich.table import Column, Table
from typer import Context, Typer

from aesop.commands.common.enums.output_format import OutputFormat
from aesop.commands.common.exception_handler import exception_handler
from aesop.commands.common.options import OutputFormatOption
from aesop.config import AesopConfig
from aesop.graphql.generated.get_dataset_custom_metadata import (
    GetDatasetCustomMetadataNodeDataset,
)
from aesop.graphql.generated.input_types import (
    CustomMetadataItemInput,
    UpdateCustomMetadataInput,
)

app = Typer()


class _Item(BaseModel):
    key: str
    value: str


def _format_output(
    items: List[_Item],
    output_format: OutputFormat,
) -> None:
    if output_format is OutputFormat.JSON:
        print_json(TypeAdapter(List[_Item]).dump_json(items).decode())

    if output_format is OutputFormat.TABULAR:
        table = Table(
            Column(header="Key", no_wrap=True, style="bold cyan"),
            "Value",
            show_lines=True,
        )
        for item in items:
            table.add_row(item.key, item.value)
        print(table)

    if output_format is OutputFormat.CSV:
        spamwriter = csv.writer(sys.stdout)
        spamwriter.writerow(["Key", "Value"])
        spamwriter.writerows([[item.key, item.value] for item in items])


@exception_handler("get custom metadata")
@app.command(help="Gets custom metadata attached to a dataset.")
def get(
    ctx: Context,
    dataset_id: str,
    output: OutputFormat = OutputFormatOption,
) -> None:
    config: AesopConfig = ctx.obj
    node = config.get_graphql_client().get_dataset_custom_metadata(dataset_id).node
    assert isinstance(node, GetDatasetCustomMetadataNodeDataset)
    metadata = node.custom_metadata.metadata if node.custom_metadata else []
    _format_output(
        [_Item(key=item.key, value=item.value) for item in metadata],
        output,
    )


@exception_handler("update custom metadata")
def _update(
    config: AesopConfig,
    output: OutputFormat,
    dataset_id: str,
    set: Dict[str, str] = {},
    unset: List[str] = [],
) -> None:
    # Custom metadata values must be valid json
    for value in set.values():
        try:
            json.loads(value)
        except Exception:
            raise ValueError(
                f"Custom metadata value must be valid JSON string: {value}"
            )

    metadata = (
        config.get_graphql_client()
        .update_dataset_custom_metadata(
            UpdateCustomMetadataInput(
                entityId=dataset_id,
                set=(
                    [
                        CustomMetadataItemInput(key=key, value=value)
                        for key, value in set.items()
                    ]
                    if set
                    else None
                ),
                unset=unset if unset else None,
            )
        )
        .update_custom_metadata.metadata
    )
    _format_output(
        [_Item(key=item.key, value=item.value) for item in metadata],
        output,
    )


@exception_handler("add custom metadata")
@app.command(help="Adds a custom metadata to a dataset.")
def add(
    ctx: Context,
    dataset_id: str,
    key: str,
    value: str,
    output: OutputFormat = OutputFormatOption,
) -> None:
    _update(ctx.obj, output, dataset_id, {key: value})


@exception_handler("remove custom metadata")
@app.command(help="Removes a custom metadata from a dataset.")
def remove(
    ctx: Context,
    dataset_id: str,
    key: str,
    output: OutputFormat = OutputFormatOption,
) -> None:
    _update(ctx.obj, output, dataset_id, unset=[key])
