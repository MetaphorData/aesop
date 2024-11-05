from typing import List, Optional

from pydantic import TypeAdapter
from rich import print, print_json
from typer import Context, Typer

from aesop.commands.common.enums.output_format import OutputFormat
from aesop.commands.common.exception_handler import exception_handler
from aesop.commands.common.options import OutputFormatOption
from aesop.commands.common.paginator import ClientQueryCallback, paginate_query
from aesop.config import AesopConfig
from aesop.console import console
from aesop.graphql.generated.enums import NamespaceType
from aesop.graphql.generated.get_namespaces import (
    GetNamespaces,
    GetNamespacesNamespacesEdges,
    GetNamespacesNamespacesEdgesNode,
)
from aesop.graphql.generated.input_types import NamespaceDescriptionInput

from .assets import app as assets_app
from .saved_queries import app as saved_queries_app

app = Typer(help="Manages data domains in Metaphor.")
app.add_typer(assets_app, name="assets")
app.add_typer(saved_queries_app, name="saved-queries")


@exception_handler("Add domain")
@app.command(help="Adds a data domain.")
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


@exception_handler("list domains")
@app.command(help="Lists data domains.", name="list")
def list_(
    ctx: Context,
    name: Optional[str] = None,
    parent_id: Optional[str] = None,
) -> None:
    config: AesopConfig = ctx.obj

    callback: ClientQueryCallback[GetNamespaces] = (
        lambda client, end_cursor: client.get_namespaces(
            NamespaceType.DATA_GROUP,
            name,
            [parent_id] if parent_id else None,
            end_cursor,
        )
    )

    # Need this for mypy to work
    def edge_to_node(
        edge: GetNamespacesNamespacesEdges,
    ) -> GetNamespacesNamespacesEdgesNode:
        return edge.node

    nodes = list(
        paginate_query(
            config,
            callback,
            lambda resp: resp.namespaces.edges,
            lambda resp: resp.namespaces.page_info,
            edge_to_node,
        )
    )
    print_json(
        TypeAdapter(List[GetNamespacesNamespacesEdgesNode]).dump_json(nodes).decode()
    )


@exception_handler("remove domain")
@app.command(help="Removes a data domain.")
def remove(
    ctx: Context,
    id: str,
) -> None:
    config: AesopConfig = ctx.obj
    resp = config.get_graphql_client().delete_domain(id).delete_namespaces
    if resp.deleted_ids:
        console.ok(f"Deleted domains: {resp.deleted_ids}")
    if resp.failed_ids:
        console.warning(f"Failed to delete domain: {resp.failed_ids[0]}")
