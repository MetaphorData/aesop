from typing import List, Optional

from pydantic import BaseModel, model_validator

from aesop.commands.common.paginator import ClientQueryCallback, paginate_query
from aesop.graphql.generated.client import Client
from aesop.graphql.generated.get_namespace import (
    GetNamespace,
    GetNamespaceNamespacesEdges,
    GetNamespaceNamespacesEdgesNode,
)
from aesop.graphql.generated.input_types import HashtagInput


def create_data_document(
    client: Client,
    title: str,
    content: str,
    hashtags: Optional[List[str]],
    publish: bool,
) -> str:
    """
    Creates a data document. Returns the document's id.
    """
    hashtag_inputs = (
        [HashtagInput(value=value) for value in hashtags] if hashtags else None
    )
    res = client.create_data_document(
        title, content, publish, hashtag_inputs
    ).create_knowledge_card
    assert res
    return res.id


class Directory(BaseModel):
    """
    Splits the raw directory path into parts. It is possible to do more sophisticated
    path validation.
    """

    dir: str
    directories: List[str] = []

    @model_validator(mode="after")
    def populate_directories(self) -> "Directory":
        self.directories = [x.strip() for x in self.dir.split("/") if x.strip()]
        return self


def get_namespace_id(
    client: Client,
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
        client,
        callback,
        lambda resp: resp.namespaces.edges,
        lambda resp: resp.namespaces.page_info,
        edge_to_node,
    ):
        if node.namespace_info and node.namespace_info.name == name:
            # Return on the first exact match, impossible to have more than one.
            return node.id
    return None


def create_namespace(
    client: Client,
    directory: Directory,
) -> Optional[str]:
    """
    Creates the namespace. In `directory` we have a list of directory parts, to ensure
    the whole path exists, we traverse from the start to the first subdirectory that
    does not exist, and create every single subdirectory that follows it.
    """
    parent_id: Optional[str] = None

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

        namespace_id = get_namespace_id(client, name, parent_id)
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


def attach_document_to_namespace(
    client: Client,
    namespace_id: str,
    document_id: str,
) -> None:
    """
    Attaches the document to the namespace.
    """
    client.attach_data_document_to_namespace(namespace_id, document_id)
