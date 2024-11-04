from rich import print
from typer import Context, Typer

from aesop.commands.common.exception_handler import exception_handler
from aesop.config import AesopConfig
from aesop.console import console

app = Typer(help="Manages data documents on Metaphor.")


@exception_handler("create document")
@app.command(help="Creates a data document.")
def create(
    ctx: Context,
    name: str,
    content: str,
) -> None:
    config: AesopConfig = ctx.obj
    resp = (
        config.get_graphql_client()
        .create_data_document(name=name, content=content, publish=True)
        .create_knowledge_card
    )
    assert resp
    url = config.url / "document" / resp.id.split("~", maxsplit=1)[-1]
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
