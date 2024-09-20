from typing import Optional

import typer

from aesop.commands.common.enums.output_format import OutputFormat

from .commands.list import list as list_command

app = typer.Typer()


@app.command()
def list(
    ctx: typer.Context,
    name: Optional[str] = typer.Option(
        default=None,
        help="Name of the governed tag",
    ),
    output: OutputFormat = typer.Option(
        default=OutputFormat.TABULAR,
        help=f"The output format. Supported formats: [{', '.join(f for f in OutputFormat)}]",
    ),
):
    list_command(name, output, ctx.obj)
