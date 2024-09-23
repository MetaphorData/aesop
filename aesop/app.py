import typer
import yaml
from typing_extensions import Annotated

from aesop.commands import info_command, tags_app, upload_command
from aesop.commands.common.enums.output_format import OutputFormat
from aesop.config import DEFAULT_CONFIG_PATH, AesopConfig

app = typer.Typer(add_completion=False)
app.add_typer(tags_app, name="tags")


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


@app.callback()
def main(
    ctx: typer.Context,
    config_file: Annotated[
        typer.FileText, typer.Option(help="Path to the configuration file.")
    ] = DEFAULT_CONFIG_PATH.as_posix(),  # type: ignore
) -> None:
    ctx.obj = AesopConfig.model_validate(yaml.safe_load(config_file))


if __name__ == "__main__":
    app()
