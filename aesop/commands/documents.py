from typing import List, Optional

from pydantic import BaseModel, model_validator
from rich import print
from typer import Argument, Context, FileText, Option, Typer

from aesop.commands.common.exception_handler import exception_handler
from aesop.commands.common.paginator import ClientQueryCallback, paginate_query
from aesop.config import AesopConfig
from aesop.graphql.generated.client import Client
from aesop.graphql.generated.get_namespace import (
    GetNamespace,
    GetNamespaceNamespacesEdges,
    GetNamespaceNamespacesEdgesNode,
)

app = Typer()


def _create_data_document(
    client: Client,
    title: str,
    content: str,
    publish: bool,
) -> str:
    """
    Creates a data document. Returns the document's id.
    """
    res = client.create_data_document(title, content, publish).create_knowledge_card
    assert res
    return res.id


class _Directory(BaseModel):
    """
    Splits the raw directory path into parts. It is possible to do more sophisticated
    path validation.
    """

    dir: str
    directories: List[str] = []

    @model_validator(mode="after")
    def populate_directories(self) -> "_Directory":
        self.directories = [x.strip() for x in self.dir.split("/") if x.strip()]
        return self


def _get_namespace_id(
    config: AesopConfig,
    name: str,
    parent_id: Optional[str],
) -> Optional[str]:
    """
    Locates the namespace whose name is an exact match with the given name.
    """
    callback: ClientQueryCallback[GetNamespace] = (
        lambda client, end_cursor: client.get_namespace(
            name, [parent_id] if parent_id else None, end_cursor
        )
    )

    # Need this for mypy to work
    def edge_to_node(
        edge: GetNamespaceNamespacesEdges,
    ) -> GetNamespaceNamespacesEdgesNode:
        return edge.node

    for node in paginate_query(
        config,
        callback,
        lambda resp: resp.namespaces.edges,
        lambda resp: resp.namespaces.page_info,
        edge_to_node,
    ):
        if node.namespace_info and node.namespace_info.name == name:
            # Return on the first exact match, impossible to have more than one.
            return node.id
    return None


def _create_namespace(
    config: AesopConfig,
    directory: _Directory,
) -> Optional[str]:
    """
    Creates the namespace. In `directory` we have a list of directory parts, to ensure
    the whole path exists, we traverse from the start to the first subdirectory that
    does not exist, and create every single subdirectory that follows it.
    """
    parent_id: Optional[str] = None
    client = config.get_graphql_client()

    # Flag to stop searching for the directory and just create
    should_create = False

    i: int = 0
    while i < len(directory.directories):
        name = directory.directories[i]
        i += 1
        if should_create:
            # Just create, no need to check if it exists.
            res = client.create_namespace(name, parent_id).create_namespace
            assert res
            parent_id = res.id
            continue

        namespace_id = _get_namespace_id(config, name, parent_id)
        if not namespace_id:
            # There's no directory that's called `name`, need to create it.
            # Not updating parent_id, need to toggle should_create and decrease `i`
            # by 1.
            should_create = True
            i -= 1
        else:
            # Found a directory named `name`, its namespace_id is our new parent_id
            # then.
            parent_id = namespace_id

    return parent_id


def _attach_document_to_namespace(
    client: Client,
    namespace_id: str,
    document_id: str,
) -> None:
    """
    Attaches the document to the namespace.
    """
    client.attach_data_document_to_namespace(namespace_id, document_id)


@exception_handler("sync document")
@app.command(
    help="Imports a local file to Metaphor's data document storage.", name="import"
)
def import_(
    ctx: Context,
    input_file: FileText = Argument(help="The input file to import to Metaphor."),
    directory: str = Option(
        help="The directory to import the file to. Should be in the format of a "
        "single slash-separated string. Any nonexisting subdirectory will be created.",
        default="",
    ),
    publish: bool = Option(
        help="Whether to publish the imported file or not.", default=True
    ),
) -> None:
    """
    1. Creates the target namespace if it does not exist already.
    2. Creates the data document.
    3. Attaches the data document to the target namespace.
    """
    config: AesopConfig = ctx.obj
    client = config.get_graphql_client()
    namespace_id = _create_namespace(config, _Directory(dir=directory))
    document_id = _create_data_document(
        client, input_file.name, input_file.read(), publish
    )
    if namespace_id:
        _attach_document_to_namespace(client, namespace_id, document_id)
    document_url = config.base_url / "document" / document_id.split("~")[-1]
    print(f"Created document: {document_url.human_repr()}")
