import typer

from aesop.commands.entities.datasets.commands import get_aspect_app

app = typer.Typer(help="Manage datasets in Metaphor.")
app.add_typer(get_aspect_app, name="get-aspect")
