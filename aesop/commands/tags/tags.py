from enum import Enum
from typing import Optional

import typer

from aesop.commands.common.arguments import InputFileArg
from aesop.commands.common.enums.output_format import OutputFormat
from aesop.commands.common.exception_handler import exception_handler
from aesop.commands.common.options import OutputFormatOption
from aesop.commands.tags.models import (
    BatchAddTagsInput,
    BatchAssignTagsInput,
    BatchRemoveTagsInput,
)

from .commands.add import add as add_command
from .commands.add import batch_add as batch_add_command
from .commands.assign import assign as assign_command
from .commands.assign import batch_assign as batch_assign_command
from .commands.get import get as get_command
from .commands.remove import batch_remove as batch_remove_command
from .commands.remove import remove as remove_command
from .commands.unassign import batch_unassign as batch_unassign_command
from .commands.unassign import unassign as unassign_command

app = typer.Typer(help="Manage tags in Metaphor.")


class TagsRichPanelNames(str, Enum):
    add = "Adding tags"
    assign = "Assigning tags"
    get = "Listing tags"
    remove = "Removing tags"
    unassign = "Unassigning tags"


@app.command(
    help="Add a single governed tag with optional description text to Metaphor.",
    rich_help_panel=TagsRichPanelNames.add,
)
@exception_handler("add tag")
def add(
    ctx: typer.Context,
    name: str,
    description: Optional[str] = typer.Argument(default=None),
) -> None:
    add_command(name, description, ctx.obj)


@app.command(
    help="Batch add governed tags with optional description text to Metaphor.",
    rich_help_panel=TagsRichPanelNames.add,
)
@exception_handler("batch add tags")
def batch_add(
    ctx: typer.Context,
    input_file: typer.FileText = InputFileArg(BatchAddTagsInput),
) -> None:
    batch_add_command(BatchAddTagsInput.model_validate_json(input_file.read()), ctx.obj)


@app.command(
    help="Assign a governed tag to an asset.",
    rich_help_panel=TagsRichPanelNames.assign,
)
@exception_handler("assign tag")
def assign(
    ctx: typer.Context,
    tag_id: str,
    asset_id: str,
) -> None:
    assign_command(tag_id, asset_id, ctx.obj)


@app.command(
    help="Batch assign governed tags to multiple assets",
    rich_help_panel=TagsRichPanelNames.assign,
)
@exception_handler("batch assign tags")
def batch_assign(
    ctx: typer.Context,
    input_file: typer.FileText = InputFileArg(BatchAssignTagsInput),
) -> None:
    batch_assign_command(
        BatchAssignTagsInput.model_validate_json(input_file.read()), ctx.obj
    )


@app.command(
    help="Get governed tags.",
    rich_help_panel=TagsRichPanelNames.get,
)
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


@app.command(
    help="Remove a governed tag from Metaphor.",
    rich_help_panel=TagsRichPanelNames.remove,
)
@exception_handler("remove tag")
def remove(
    tag_id: str,
    ctx: typer.Context,
) -> None:
    remove_command(tag_id, ctx.obj)


@app.command(
    help="Batch remove governed tags from Metaphor.",
    rich_help_panel=TagsRichPanelNames.remove,
)
@exception_handler("batch remove tags")
def batch_remove(
    ctx: typer.Context,
    input_file: typer.FileText = InputFileArg(BatchRemoveTagsInput),
) -> None:
    batch_remove_command(
        BatchRemoveTagsInput.model_validate_json(input_file.read()), ctx.obj
    )


@app.command(
    help="Unassign a governed tag from an asset.",
    rich_help_panel=TagsRichPanelNames.unassign,
)
@exception_handler("unassign tag")
def unassign(
    ctx: typer.Context,
    tag_id: str,
    asset_id: str,
) -> None:
    unassign_command(tag_id, asset_id, ctx.obj)


@app.command(
    help="Unassign governed tags from assets.",
    rich_help_panel=TagsRichPanelNames.unassign,
)
@exception_handler("batch unassign tags")
def batch_unassign(
    ctx: typer.Context,
    input_file: typer.FileText = InputFileArg(BatchAssignTagsInput),
) -> None:
    batch_unassign_command(
        BatchAssignTagsInput.model_validate_json(input_file.read()), ctx.obj
    )
