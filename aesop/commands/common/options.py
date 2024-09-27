import typer

from aesop.commands.common.enums.output_format import OutputFormat

OutputFormatOption = typer.Option(
    default=OutputFormat.JSON,
    help="The output format."
    f"Supported formats: [{', '.join(f for f in OutputFormat)}]",
)
