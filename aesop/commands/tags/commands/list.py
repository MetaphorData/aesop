import csv
import json
import sys
from dataclasses import dataclass
from typing import List, Optional

from pydantic import BaseModel
from rich.table import Column, Table

from aesop.commands.common.enums.output_format import OutputFormat
from aesop.commands.common.exception_handler import exception_handler
from aesop.config import AesopConfig
from aesop.console import console
from aesop.graphql.generated.custom_fields import (
    PageInfoFields,
    UserDefinedResourceConnectionFields,
    UserDefinedResourceDescriptionFields,
    UserDefinedResourceEdgeFields,
    UserDefinedResourceFields,
    UserDefinedResourceInfoFields,
)
from aesop.graphql.generated.custom_queries import Query
from aesop.graphql.generated.input_types import ResourceInfoConnectionFilterInput


def _get_query(end_cursor: Optional[str], name: Optional[str]):
    return Query.user_defined_resources(
        filters=ResourceInfoConnectionFilterInput(
            type=["GOVERNED_TAG"],
            name=name,
        ),
        first=50,
        after=end_cursor,
    ).fields(
        UserDefinedResourceConnectionFields.edges().fields(
            UserDefinedResourceEdgeFields.node().fields(
                UserDefinedResourceFields.id,
                UserDefinedResourceFields.userDefinedResourceInfo().fields(
                    UserDefinedResourceInfoFields.name,
                    UserDefinedResourceInfoFields.description().fields(
                        UserDefinedResourceDescriptionFields.text,
                    ),
                ),
            )
        ),
        UserDefinedResourceConnectionFields.pageInfo().fields(
            PageInfoFields.endCursor,
            PageInfoFields.hasNextPage,
        ),
    )


class _Node(BaseModel):
    id: str
    name: str
    description: Optional[str] = None


def _paginate_queries(config: AesopConfig, name: str):
    client = config.get_graphql_client()
    nodes: List[_Node] = []
    has_next_page = True
    end_cursor = None
    while has_next_page:
        query = _get_query(end_cursor, name)
        resp = client.query(query, operation_name="listGovernedTags")
        user_defined_resources = resp["userDefinedResources"]
        edges = [edge["node"] for edge in user_defined_resources["edges"]]
        page_info = user_defined_resources["pageInfo"]
        end_cursor = page_info["endCursor"]
        has_next_page = page_info["hasNextPage"]
        nodes.extend(
            _Node(
                id=edge["id"],
                name=edge["userDefinedResourceInfo"]["name"],
                description=(
                    edge["userDefinedResourceInfo"]["description"]["text"]
                    if edge["userDefinedResourceInfo"]["description"]
                    and edge["userDefinedResourceInfo"]["description"]["text"]
                    else None
                ),
            )
            for edge in edges
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
            Column(header="ID", no_wrap=True, style="bold cyan"), "Name", "Description", show_lines=True
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
