from typing import Optional

import typer

from aesop.commands.common.arguments import InputFileArg
from aesop.commands.common.enums.output_format import OutputFormat
from aesop.commands.common.exception_handler import exception_handler
from aesop.commands.common.options import OutputFormatOption
from aesop.commands.tags.models import AddTagsInput, RemoveTagsInput

from .commands.add import add as add_command
from .commands.assign import assign as assign_command
from .commands.get import get as get_command
from .commands.remove import remove as remove_command

app = typer.Typer(help="Manage tags in Metaphor.")


@app.command(help="Attaches governed tags to entities.")
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


@app.command(help="Add governed tags with optional description text to Metaphor.")
@exception_handler("add tags")
def add(
    ctx: typer.Context,
    input_file: typer.FileText = InputFileArg(AddTagsInput),
) -> None:
    add_command(AddTagsInput.model_validate_json(input_file.read()), ctx.obj)


@app.command(help="Removes governed tags from Metaphor.")
@exception_handler("remove tags")
def remove(
    ctx: typer.Context,
    input_file: typer.FileText = InputFileArg(RemoveTagsInput),
) -> None:
    remove_command(RemoveTagsInput.model_validate_json(input_file.read()), ctx.obj)


@app.command(help="Get governed tags.")
@exception_handler("get tags")
def get(
    ctx: typer.Context,
    name: Optional[str] = typer.Option(
        default=None,
        help="Filter for the name of the governed tag",
    ),
    output: OutputFormat = OutputFormatOption,
) -> None:
    get_command(name, output, ctx.obj)
