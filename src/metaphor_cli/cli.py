# metaphor_cli/cli.py

import asyncio
import typer
from rich.console import Console
from rich.prompt import Prompt
from metaphor_cli.config import Config
from metaphor_cli.data_asset_loaders import load_data_assets_from_csv
from metaphor_cli.input_validation import validate_data_asset, validate_upload_domain
from metaphor_cli.data_asset_uploaders import upload_knowledge_card

app = typer.Typer(add_completion=False)
console = Console()
config = Config()

def main_menu():
    """
    Show the main menu to the user to choose which operation to perform.
    """
    console.print("[bold magenta]Welcome to the Metaphor CLI Tool![/bold magenta]")
    console.print("1: Upload data assets from a CSV file")
    console.print("2: Exit")
    
    choice = Prompt.ask("Please choose an operation", choices=["1", "2"], default="1")
    
    if choice == "1":
        upload_interactive()
    elif choice == "2":
        console.print("[bold cyan]Exiting...[/bold cyan]")
        raise typer.Exit()

def upload_interactive():
    """
    Interactive function to gather upload information and perform the upload.
    """
    csv_path = Prompt.ask("Path to the CSV file containing data asset information")
    api_key = Prompt.ask("Your GraphQL API key. (Not Shown)", password=True)
    upload_domain = Prompt.ask("Metaphor domain for upload, the part before 'metaphor.io' in the URL without the https://")
    
    config.api_key = api_key
    config.upload_domain = upload_domain

    try:
        data_assets = load_data_assets_from_csv(csv_path)
        data_assets_upload = []
        for asset in data_assets:
            if validate_data_asset(asset):
                data_assets_upload.append(asset)
            else:
                console.print(f"[bold yellow]Skipping invalid asset: {asset}[/bold yellow]")
        asyncio.run(upload_assets(data_assets_upload, config))
        console.print("[green]Data assets uploaded successfully[/green]")
    except Exception as e:
        console.print(f"[bold red]An error occurred: {str(e)}[/bold red]")
        raise typer.Exit(code=1)

async def upload_assets(data_assets, config):
    for asset in data_assets:
        asset_type = asset.pop("type", "").upper()  # Remove 'type' and get its value
        if asset_type == "KNOWLEDGE_CARD":
            await upload_knowledge_card(asset, config.api_key, config.upload_domain)
        else:
            console.print(f"[yellow]Skipping asset with unsupported type: {asset['type']}[/yellow]")

@app.command()
def upload(
    csv_path: str = typer.Option(..., help="Path to the CSV file containing data asset information"),
    api_key: str = typer.Option(..., help="Your GraphQL API key"),
    upload_domain: str = typer.Option(..., help="Metaphor domain for upload")
):
    """
    Command-line interface for uploading data assets from a CSV file.
    """
    validate_upload_domain(upload_domain)
    config.api_key = api_key
    config.upload_domain = upload_domain

    try:
        data_assets = load_data_assets_from_csv(csv_path)
        asyncio.run(upload_assets(data_assets, config))
        console.print("[green]Data assets uploaded successfully[/green]")
    except Exception as e:
        console.print(f"[bold red]An error occurred: {str(e)}[/bold red]")
        raise typer.Exit(code=1)

@app.callback(invoke_without_command=True)
def callback(ctx: typer.Context):
    """
    Metaphor CLI for uploading data assets.
    """
    if ctx.invoked_subcommand is None:
        main_menu()

if __name__ == "__main__":
    
    app()