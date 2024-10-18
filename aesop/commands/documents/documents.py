from typer import Typer

from aesop.commands.documents import biz_glossary

app = Typer()
app.add_typer(biz_glossary.app, name="biz-glossary")
