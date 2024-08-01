import typer
from rich.console import Console

from aesop.api_key_utils import load_api_key, save_api_key
from aesop.data_asset_loaders import SUPPORTED_DATA_ASSETS
from aesop.data_asset_uploaders import perform_upload

app = typer.Typer(add_completion=False)
console = Console()


@app.callback()
def main(ctx: typer.Context):
    ctx.ensure_object(dict)
    api_key = load_api_key()
    if not api_key:
        api_key = typer.prompt("Your GraphQL API key", hide_input=True)
        save_key = typer.confirm("Do you want to save this API key for future use?")
        if save_key:
            save_api_key(api_key)
            console.print("[green]API key saved successfully.[/green]")
    ctx.obj["api_key"] = api_key


@app.command()
def upload(
    ctx: typer.Context,
    csv_path: str = typer.Option(
        ..., help="Path to the CSV file containing data asset information"
    ),
    upload_domain: str = typer.Option(
        ...,
        help=(
            "Metaphor domain for upload, the part "
            "before 'metaphor.io' in the URL without the https://"
        ),
    ),
):
    f"""
    Upload data assets from a CSV file.
    Supported data asset types: {', '.join(SUPPORTED_DATA_ASSETS.keys())}
    """
    perform_upload(csv_path, ctx.obj["api_key"], upload_domain)


@app.command()
def api_key(
    api_key: str = typer.Option(..., prompt=True, hide_input=True, help="Your GraphQL API key")
):
    """
    Save or update the API key.
    """
    save_api_key(api_key)
    console.print("[green]API key saved successfully.[/green]")


if __name__ == "__main__":
    app()
