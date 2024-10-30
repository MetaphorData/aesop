from rich import print
from typer import Context, Typer

from aesop.commands.common.exception_handler import exception_handler
from aesop.config import AesopConfig

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
