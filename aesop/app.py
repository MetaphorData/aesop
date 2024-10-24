import glob
from enum import Enum
from importlib import metadata
from pathlib import Path

import typer
import yaml
from rich import print
from rich.markdown import Markdown
from typing_extensions import Annotated

from aesop.commands import (
    datasets_app,
    domains_app,
    glossaries_app,
    info_command,
    settings_app,
    tags_app,
    upload_command,
    webhooks_app,
)
from aesop.commands.common.enums.output_format import OutputFormat
from aesop.commands.common.exception_handler import exception_handler
from aesop.config import DEFAULT_CONFIG_PATH, AesopConfig

app = typer.Typer(add_completion=False, rich_markup_mode="markdown")
app.add_typer(datasets_app, name="datasets")
app.add_typer(domains_app, name="domains")
app.add_typer(glossaries_app, name="glossaries")
app.add_typer(settings_app, name="settings")
app.add_typer(tags_app, name="tags")
app.add_typer(webhooks_app, name="webhooks")


@app.command()
def info(
    ctx: typer.Context,
    output: OutputFormat = typer.Option(
        default=OutputFormat.TABULAR,
        help="The output format. "
        f"Supported formats: [{', '.join(f for f in OutputFormat)}]",
    ),
) -> None:
    "Display information about the Metaphor instance."
    info_command(output, ctx.obj)


@app.command()
def upload(
    ctx: typer.Context,
    csv_path: str = typer.Argument(
        ...,
        help="Path to the CSV file containing data asset information",
    ),
) -> None:
    """
    Upload data assets from a CSV file.
    """
    upload_command(csv_path, ctx.obj)


@app.command()
def version() -> None:
    """
    Print Aesop's version.
    """
    print(f"Aesop version: {metadata.version('metaphor-aesop')}")


root_path = Path(__file__).parent.resolve()  # This is the aesop app directory
commands_path = root_path / "docs" / "commands"
CommandsWithHelpDoc = Enum(  # type: ignore
    "CommandsWithHelpDoc",
    {
        f"v_{v}": v
        for v in [
            Path(filename).stem
            for filename in glob.glob((commands_path / "*.md").as_posix())
        ]
    },
)


@app.command()
def help(
    command: CommandsWithHelpDoc,  # type: ignore
) -> None:
    """
    Print help for a command.
    """
    command_name: str = command.value
    with open(commands_path / f"{command_name}.md") as f:
        print(Markdown(f.read()))


@app.callback()
@exception_handler("main")
def main(
    ctx: typer.Context,
    config_file: Annotated[
        typer.FileText, typer.Option(help="Path to the configuration file.")
    ] = DEFAULT_CONFIG_PATH.as_posix(),  # type: ignore
) -> None:
    ctx.obj = AesopConfig.model_validate(yaml.safe_load(config_file))


if __name__ == "__main__":
    app()
