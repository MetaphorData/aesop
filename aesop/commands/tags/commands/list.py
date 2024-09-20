import csv
import sys
from typing import List, Optional

from pydantic import BaseModel
from rich.table import Column, Table

from aesop.commands.common.enums.output_format import OutputFormat
from aesop.commands.common.exception_handler import exception_handler
from aesop.config import AesopConfig
from aesop.console import console


class _Node(BaseModel):
    id: str
    name: str
    description: Optional[str] = None


def _paginate_queries(config: AesopConfig, name: Optional[str]):
    client = config.get_graphql_client()
    nodes: List[_Node] = []
    has_next_page = True
    end_cursor = None
    while has_next_page:
        resp = client.list_governed_tags(name, end_cursor=end_cursor)
        edges = resp.user_defined_resources.edges
        page_info = resp.user_defined_resources.page_info
        end_cursor = page_info.end_cursor
        has_next_page = page_info.has_next_page
        nodes.extend(
            _Node(
                id=edge.node.id,
                name=edge.node.user_defined_resource_info.name,
                description=(
                    edge.node.user_defined_resource_info.description.text
                    if edge.node.user_defined_resource_info.description
                    and edge.node.user_defined_resource_info.description.text
                    else None
                ),
            )
            for edge in edges
            if edge is not None
        )
    return nodes


@exception_handler("list tags", exception_type=Exception)
def list(
    name: Optional[str],
    output: OutputFormat,
    config: AesopConfig,
) -> None:
    res = _paginate_queries(config, name)
    if output is OutputFormat.TABULAR:
        table = Table(
            Column(header="ID", no_wrap=True, style="bold cyan"),
            "Name",
            "Description",
            show_lines=True,
        )
        for node in res:
            table.add_row(node.id, node.name, node.description)
        console.print(table)
    elif output is OutputFormat.CSV:
        spamwriter = csv.writer(sys.stdout)
        spamwriter.writerow(["ID", "Name", "Description"])
        spamwriter.writerows([[node.id, node.name, node.description] for node in res])
    elif output is OutputFormat.JSON:
        console.print([node.model_dump() for node in res])
