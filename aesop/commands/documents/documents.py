from typer import Typer

from aesop.commands.documents import biz_glossary

app = Typer(help="Manages data documents in Metaphor.")
app.add_typer(biz_glossary.app, name="biz-glossary")
