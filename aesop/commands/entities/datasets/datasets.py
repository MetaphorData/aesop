import typer

from aesop.commands.entities.datasets.commands import get_aspect_app
from aesop.commands.entities.datasets.commands import generate_ai_descriptions

app = typer.Typer(help="Manage datasets in Metaphor.")
app.add_typer(get_aspect_app, name="get-aspect")
app.add_typer(generate_ai_descriptions, name="generate-ai-descriptions")

