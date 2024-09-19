from dataclasses import dataclass
from typing import List, Optional

from rich.table import Column, Table

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


def get_query(end_cursor: Optional[str]):
    return Query.user_defined_resources(
        filters=ResourceInfoConnectionFilterInput(
            type=["GOVERNED_TAG"],
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


@dataclass
class Node:
    id: str
    name: str
    description: Optional[str] = None


def paginate_queries(config: AesopConfig):
    client = config.get_graphql_client()
    nodes: List[Node] = []
    has_next_page = True
    end_cursor = None
    while has_next_page:
        query = get_query(end_cursor)
        resp = client.query(query, operation_name="listGovernedTags")
        user_defined_resources = resp["userDefinedResources"]
        edges = [edge["node"] for edge in user_defined_resources["edges"]]
        page_info = user_defined_resources["pageInfo"]
        end_cursor = page_info["endCursor"]
        has_next_page = page_info["hasNextPage"]
        nodes.extend(
            Node(
                id=edge["id"],
                name=edge["userDefinedResourceInfo"]["name"],
                description=(
                    edge["userDefinedResourceInfo"]["description"]["text"]
                    if edge["userDefinedResourceInfo"]["description"]
                    else None
                ),
            )
            for edge in edges
        )
    return nodes


@exception_handler("list tags", exception_type=Exception)
def list(
    config: AesopConfig,
) -> None:
    res = paginate_queries(config)
    table = Table(
        Column(header="ID", no_wrap=True, style="bold"), "Name", "Description", show_lines=True
    )
    for node in res:
        table.add_row(node.id, node.name, node.description)
    console.print(table)
