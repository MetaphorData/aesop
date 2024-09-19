import typer

from .commands.list import list as list_command

app = typer.Typer()


@app.command()
def list(
    ctx: typer.Context,
):
    list_command(ctx.obj)
