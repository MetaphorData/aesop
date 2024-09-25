import typer

from .custom_metadata.custom_metadata import app as custom_metadata_app
from .non_prod.non_prod import app as non_prod_app
from .soft_deletion.soft_deletion import app as soft_deletion_app

app = typer.Typer(help="Manage settings in Metaphor.")
app.add_typer(non_prod_app, name="non-prod")
app.add_typer(custom_metadata_app, name="custom-metadata")
app.add_typer(soft_deletion_app, name="soft-deletion")
