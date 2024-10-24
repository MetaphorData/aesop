import csv
import json
import sys
from typing import List, Optional, Union

from pydantic import BaseModel
from rich.table import Column, Table

from aesop.commands.common.enums.output_format import OutputFormat
from aesop.console import console
from aesop.graphql.generated.get_governed_tag import (
    GetGovernedTagNodeUserDefinedResource,
)
from aesop.graphql.generated.get_governed_tag_child_tags import (
    GetGovernedTagChildTagsNodeUserDefinedResourceChildResourcesEdgesNode,
)
from aesop.graphql.generated.list_governed_tags import (
    ListGovernedTagsUserDefinedResourcesEdgesNode,
)


class GovernedTagParent(BaseModel):
    id: str
    name: Optional[str]


class GovernedTagNode(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    parent: Optional[GovernedTagParent] = None

    @classmethod
    def from_gql_response(
        cls,
        node: Union[
            ListGovernedTagsUserDefinedResourcesEdgesNode,
            GetGovernedTagNodeUserDefinedResource,
            GetGovernedTagChildTagsNodeUserDefinedResourceChildResourcesEdgesNode,
        ],
    ) -> Optional["GovernedTagNode"]:
        if not node.user_defined_resource_info:
            return None

        parent = (
            GovernedTagParent(
                id=node.parent_resource.id,
                name=(
                    node.parent_resource.user_defined_resource_info.name
                    if node.parent_resource.user_defined_resource_info
                    else None
                ),
            )
            if node.parent_resource
            else None
        )
        return GovernedTagNode(
            id=node.id,
            name=node.user_defined_resource_info.name,
            description=(
                node.user_defined_resource_info.description.text
                if node.user_defined_resource_info.description
                and node.user_defined_resource_info.description.text
                else None
            ),
            parent=parent,
        )


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
