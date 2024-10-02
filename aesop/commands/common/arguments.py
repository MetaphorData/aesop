import sys
from typing import Any

import typer
from rich.markdown import Markdown
from rich.panel import Panel

from aesop.commands.common.models import InputModel
from aesop.console import console


def _validate_input_file(
    input_model: type[InputModel], input_file: typer.FileText
) -> typer.FileText:
    if input_file.name == "<stdin>" and input_file.isatty():
        # Got nothing, print example and exit
        example_contents = ["```json"]
        example_contents.extend(input_model.example_json(indent=2).splitlines())
        example_contents.append("```")
        example_panel = Panel(
            Markdown("\n".join(example_contents)),
            title="[green][bold]Example input",
            title_align="left",
        )
        console.print(example_panel)

        commands = " ".join(sys.argv[1:])
        usage_contents = [
            "Pipe the JSON body into the command:",
            "",
            "```bash",
            f"$ cat {''.join(input_model.example_json(indent=0).splitlines())} | aesop {commands}",  # noqa E501
            "```",
            "Or provide an input file to the command:",
            "```bash",
            f"$ echo {''.join(input_model.example_json(indent=0).splitlines())} > input.json",  # noqa E501
            "",
            f"$ aesop {commands} input.json",
            "```",
        ]
        usage_panel = Panel(
            Markdown("\n".join(usage_contents)),
            title="[green][bold]Usage",
            title_align="left",
        )
        console.print(usage_panel)

        raise typer.Exit(0)

    return input_file


def InputFileArg(input_model: type[InputModel]) -> Any:
    return typer.Argument(
        help="The input file to the command. "
        "Can either be piped in or passed as a command argument, "
        "otherwise an example input payload will be displayed onto the console, "
        "and the app will exit.",
        default=sys.stdin,
        callback=lambda x: _validate_input_file(input_model, x),
    )
