import csv
import json
import sys
from typing import List, Optional

from pydantic import BaseModel
from rich.table import Column, Table

from aesop.commands.common.enums.output_format import OutputFormat
from aesop.console import console


class GovernedTagNode(BaseModel):
    id: str
    name: str
    description: Optional[str] = None


def display_nodes(
    nodes: List[GovernedTagNode],
    output: OutputFormat,
) -> None:
    if output is OutputFormat.TABULAR:
        table = Table(
            Column(header="ID", no_wrap=True, style="bold cyan"),
            "Name",
            "Description",
            show_lines=True,
        )
        for node in nodes:
            table.add_row(node.id, node.name, node.description)
        console.print(table)
    elif output is OutputFormat.CSV:
        spamwriter = csv.writer(sys.stdout)
        spamwriter.writerow(["ID", "Name", "Description"])
        spamwriter.writerows([[node.id, node.name, node.description] for node in nodes])
    elif output is OutputFormat.JSON:
        console.print_json(
            json.dumps([node.model_dump(exclude_none=True) for node in nodes]), indent=2
        )
