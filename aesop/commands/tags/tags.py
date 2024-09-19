from typing import Optional

import typer

from .commands.list import list as list_command

app = typer.Typer()


@app.command()
def list(
    ctx: typer.Context,
    name: Optional[str] = typer.Option(
        default=None,
        help="Name of the governed tag",
    ),
):
    list_command(name, ctx.obj)
