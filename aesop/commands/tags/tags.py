from typing import Optional

import typer

from aesop.commands.common.enums.output_format import OutputFormat

from .commands.add import add as add_command
from .commands.assign import assign as assign_command
from .commands.list import list as list_command

app = typer.Typer()


@app.command(help="Attaches a governed tag to an entity.")
def assign(
    ctx: typer.Context,
    entity_id: str = typer.Argument(
        help="The target entity's ID",
    ),
    tag_id: str = typer.Argument(
        help="ID of the tag to assign",
    ),
) -> None:
    assign_command(entity_id, tag_id, ctx.obj)


@app.command(help="Adds a governed tag with optional description text.")
def add(
    ctx: typer.Context,
    name: str = typer.Argument(
        help="Name of the tag",
    ),
    description: Optional[str] = typer.Argument(
        default=None, help="Description for the tag. Optional"
    ),
) -> None:
    add_command(name, description, ctx.obj)


@app.command(help="Lists all governed tags.")
def list(
    ctx: typer.Context,
    name: Optional[str] = typer.Option(
        default=None,
        help="Name of the governed tag",
    ),
    output: OutputFormat = typer.Option(
        default=OutputFormat.TABULAR,
        help="The output format."
        f"Supported formats: [{', '.join(f for f in OutputFormat)}]",
    ),
) -> None:
    list_command(name, output, ctx.obj)
