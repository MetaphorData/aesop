import json
import sys
from csv import DictReader, DictWriter, writer
from typing import Any, List, Optional, Union

from pydantic import BaseModel, Field, field_validator
from rich import print, print_json
from rich.table import Table
from typer import Argument, Context, FileText, FileTextWrite, Option, Typer

from aesop.commands.common.enums.output_format import OutputFormat
from aesop.commands.common.exception_handler import exception_handler
from aesop.commands.common.options import OutputFormatOption
from aesop.commands.documents.utils import (
    Directory,
    attach_document_to_namespace,
    create_data_document,
    create_namespace,
)
from aesop.config import AesopConfig

app = Typer()


class Columns(BaseModel):
    name: str = Field(
        description="The name of the glossary term. Should be a non-empty string."
    )
    content: str = Field(
        description="The content for the glossary term. Should be a non-empty string."
    )
    hashtags_: Union[Optional[List[str]], str] = Field(
        default=None,
        alias="hashtags",
        description="The hashtags to append to the glossary term. Should be a list "
        "of strings, or null if there is no hashtag.",
    )

    @field_validator("hashtags_", mode="after")
    @classmethod
    def validate_optional_field(cls, value: Any) -> Optional[Any]:
        if isinstance(value, str):
            return None
        return value

    @property
    def hashtags(self) -> Optional[List[str]]:
        if isinstance(self.hashtags_, str):
            raise ValueError
        if not self.hashtags_:
            return None
        return self.hashtags_


@app.command(
    help="Generates a template of business glossary CSV file with some example values."
)
def gen_template(
    file: FileTextWrite = Argument(
        default="biz_glossary.csv", help="The file to write to."
    )
) -> None:
    writer = DictWriter(file, [v.alias or k for k, v in Columns.model_fields.items()])
    writer.writeheader()
    writer.writerow(
        Columns(name="john.doe", content="some content").model_dump(by_alias=True)
    )
    writer.writerow(
        Columns(
            name="jane.doe", content="some other content", hashtags=["tag1", "tag2"]
        ).model_dump(by_alias=True)
    )
    print(f"Wrote template to {file.name}")


@app.command(help="Prints the expected schema for a business glossary CSV file.")
def schema(output_format: OutputFormat = OutputFormatOption) -> None:
    if output_format is OutputFormat.JSON:
        print_json(json.dumps(Columns.model_json_schema()))

    else:
        if output_format is OutputFormat.CSV:
            spamwriter = writer(sys.stdout)
            spamwriter.writerow(["Name", "Description"])
            for name, field in Columns.model_fields.items():
                spamwriter.writerow([field.alias or name, field.description])
        if output_format is OutputFormat.TABULAR:
            table = Table(
                "Name",
                "Description",
                show_lines=True,
            )
            for name, field in Columns.model_fields.items():
                table.add_row(field.alias or name, field.description)
            print(table)


@exception_handler("import business glossary")
@app.command(
    help="Imports a local business glossary file to Metaphor's data document storage. "
    "To see the schema or a simple template file, use `schema` or `gen-template` "
    "subcommands.",
    name="import",
)
def import_(
    ctx: Context,
    input_file: FileText = Argument(
        help="The business glossary to import to Metaphor."
    ),
    directory: str = Option(
        help="The directory to import the file to. Should be in the format of a "
        "single slash-separated string. Any nonexisting subdirectory will be created.",
        default="",
    ),
    publish: bool = Option(
        help="Whether to publish the imported file or not.", default=True
    ),
) -> None:
    """
    1. Creates the target namespace if it does not exist already.
    2. Creates the data document.
    3. Attaches the data document to the target namespace.
    """
    config: AesopConfig = ctx.obj
    client = config.get_graphql_client()
    namespace_id = create_namespace(client, Directory(dir=directory))

    files_created = 0
    for row in DictReader(input_file.readlines()):
        columns = Columns.model_validate(row)

        document_id = create_data_document(
            client, columns.name, columns.content, columns.hashtags, publish
        )

        if namespace_id:
            attach_document_to_namespace(client, namespace_id, document_id)
        files_created += 1

    if not namespace_id:
        print(f"Created {files_created} files.")
    else:
        namespace_url = config.url / "documents" / "directories" / namespace_id
        print(f"Created {files_created} files: {namespace_url.human_repr()}")
