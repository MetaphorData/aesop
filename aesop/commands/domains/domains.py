from typing import Optional

from rich import print, print_json
from typer import Context, Typer

from aesop.commands.common.enums.output_format import OutputFormat
from aesop.commands.common.exception_handler import exception_handler
from aesop.commands.common.options import OutputFormatOption
from aesop.config import AesopConfig
from aesop.console import console
from aesop.graphql.generated.input_types import NamespaceDescriptionInput

from .assets import app as assets_app
from .saved_queries import app as saved_queries_app

app = Typer()
app.add_typer(assets_app, name="assets")
app.add_typer(saved_queries_app, name="saved-queries")


@exception_handler("Add domain")
@app.command()
def add(
    ctx: Context,
    name: str,
    description: Optional[str] = None,
    tokenized_description: Optional[str] = None,
    color: Optional[str] = None,  # hex string
    icon_key: Optional[str] = None,
    parent_id: Optional[str] = None,
) -> None:
    config: AesopConfig = ctx.obj
    resp = (
        config.get_graphql_client()
        .create_domain(
            name=name,
            description=NamespaceDescriptionInput(
                text=description,
                tokenizedText=tokenized_description,
            ),
            color=color,
            icon_key=icon_key,
            parent_id=parent_id,
        )
        .create_namespace
    )
    assert resp
    print(f"Created domain: {resp.id}")


@exception_handler("get domain")
@app.command(help="Gets a data domain defined in Metaphor.")
def get(
    ctx: Context,
    id: str,
    output: OutputFormat = OutputFormatOption,
) -> None:
    config: AesopConfig = ctx.obj
    resp = config.get_graphql_client().get_domain(id).node
    if not resp:
        return

    if output is OutputFormat.JSON:
        print_json(resp.model_dump_json())


@app.command()
def remove(
    ctx: Context,
    id: str,
) -> None:
    config: AesopConfig = ctx.obj
    resp = config.get_graphql_client().delete_domain(id).delete_namespaces
    if resp.deleted_ids:
        console.ok(f"Deleted domain: {resp.deleted_ids[0]}")
    if resp.failed_ids:
        console.warning(f"Failed to delete domain: {resp.failed_ids[0]}")
