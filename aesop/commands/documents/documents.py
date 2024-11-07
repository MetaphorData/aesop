from typing import Optional

from rich import print
from typer import Argument, Context, Option, Typer

from aesop.commands.common.exception_handler import exception_handler
from aesop.commands.documents.utils import (
    Directory,
    attach_document_to_namespace,
    create_data_document,
    create_namespace,
    get_user_id,
)
from aesop.config import AesopConfig
from aesop.console import console

app = Typer(help="Manages data documents on Metaphor.")


@exception_handler("create document")
@app.command(help="Creates a data document.")
def create(
    ctx: Context,
    name: str = Argument(help="Title of the document."),
    content: str = Argument(
        help="The content of the document. To upload the content of an existing file, do `aesop documents create $(cat FILE.txt)`."
    ),
    author: Optional[str] = Option(
        help="Author of the document. If unset, a user representing the API key in use will be the document's author.",
        default=None,
    ),
    directory: str = Option(
        help="The directory to import the file to. Should be in the format of a "
        "single slash-separated string. Any nonexisting subdirectory will be created.",
        default="",
    ),
) -> None:
    config: AesopConfig = ctx.obj
    client = config.get_graphql_client()
    user_id = get_user_id(client, author) if author else None
    namespace_id = create_namespace(client, Directory(dir=directory))
    document_id = create_data_document(
        client,
        title=name,
        content=content,
        hashtags=None,
        publish=True,
        user_id=user_id,
    )

    if namespace_id:
        attach_document_to_namespace(client, namespace_id, [document_id])

    url = config.url / "document" / document_id.split("~", maxsplit=1)[-1]
    print(f"Created document: {url.human_repr()}")


@exception_handler("delete document")
@app.command(help="Deletes a data document.")
def delete(
    ctx: Context,
    id: str,
) -> None:
    config: AesopConfig = ctx.obj
    knowledge_card_prefix = "KNOWLEDGE_CARD~"
    knowledge_card_id = (
        id if id.startswith(knowledge_card_prefix) else f"{knowledge_card_prefix}{id}"
    )
    resp = (
        config.get_graphql_client()
        .delete_data_document(id=knowledge_card_id)
        .delete_knowledge_cards
    )
    if knowledge_card_id in resp.deleted_ids:
        print(f"Successfully deleted document: {id}")
    else:
        console.warning(f"Cannot delete document: {id}")
