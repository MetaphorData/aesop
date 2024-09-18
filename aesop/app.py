import typer
import yaml
from typing_extensions import Annotated

from aesop.commands.upload import upload as upload_impl
from aesop.config import DEFAULT_CONFIG_PATH, AesopConfig

app = typer.Typer(add_completion=False)


@app.command()
def upload(
    ctx: typer.Context,
    csv_path: str = typer.Argument(
        ...,
        help="Path to the CSV file containing data asset information",
    ),
):
    """
    Upload data assets from a CSV file.
    """
    upload_impl(csv_path, ctx.obj)


@app.callback()
def main(
    ctx: typer.Context,
    config_file: Annotated[
        typer.FileText, typer.Option(help="Path to the configuration file.")
    ] = DEFAULT_CONFIG_PATH.as_posix(),
):
    ctx.obj = AesopConfig.model_validate(yaml.safe_load(config_file))


if __name__ == "__main__":
    app()