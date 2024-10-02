from importlib import metadata

import typer
import yaml
from rich import print
from typing_extensions import Annotated

from aesop.commands import (
    datasets_app,
    info_command,
    settings_app,
    tags_app,
    upload_command,
)
from aesop.commands.common.enums.output_format import OutputFormat
from aesop.commands.common.exception_handler import exception_handler
from aesop.config import DEFAULT_CONFIG_PATH, AesopConfig

app = typer.Typer(add_completion=False, rich_markup_mode="markdown")
app.add_typer(tags_app, name="tags")
app.add_typer(settings_app, name="settings")
app.add_typer(datasets_app, name="datasets")


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
    print(f"Aesop version: {metadata.version('aesop')}")


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
