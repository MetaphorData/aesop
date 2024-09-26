import sys
from typing import Any

import typer
from pydantic import BaseModel

from aesop.console import console


def _validate_input_file(
    input_example: BaseModel, input_file: typer.FileText
) -> typer.FileText:
    if input_file.name == "<stdin>" and input_file.isatty():
        # Got nothing, print example and exit
        console.warning("\nExample input:")
        console.print(input_example.model_dump_json(indent=2))
        raise typer.Exit(0)

    return input_file


def InputFileArg(input_example: BaseModel) -> Any:
    return typer.Argument(
        help="The input file to the command. "
        "Can either be piped in or passed as a command argument, "
        "otherwise an example input payload will be displayed onto the console, "
        "and the app will exit.",
        default=sys.stdin,
        callback=lambda x: _validate_input_file(input_example, x),
    )
