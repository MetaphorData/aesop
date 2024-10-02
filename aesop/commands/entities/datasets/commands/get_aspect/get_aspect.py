from typing import Optional

import typer

from aesop.commands.aspects.user_defined_resources.tags.node import (
    GovernedTagNode,
    display_nodes,
)
from aesop.commands.common.enums.output_format import OutputFormat
from aesop.commands.common.exception_handler import exception_handler
from aesop.commands.common.options import OutputFormatOption
from aesop.commands.common.paginator import ClientQueryCallback, paginate_query
from aesop.graphql.generated.get_dataset_governed_tags import (
    GetDatasetGovernedTags,
    GetDatasetGovernedTagsNodeDataset,
    GetDatasetGovernedTagsNodeDatasetGovernedTagsEdges,
    GetDatasetGovernedTagsNodeDatasetGovernedTagsPageInfo,
)

app = typer.Typer(help="Display aspect of a dataset in Metaphor.")


def edge_to_node(
    edge: GetDatasetGovernedTagsNodeDatasetGovernedTagsEdges,
) -> Optional[GovernedTagNode]:
    if not edge.node.user_defined_resource_info:
        return None
    return GovernedTagNode(
        id=edge.node.id,
        name=edge.node.user_defined_resource_info.name,
        description=(
            edge.node.user_defined_resource_info.description.text
            if edge.node.user_defined_resource_info.description
            and edge.node.user_defined_resource_info.description.text
            else None
        ),
    )


@app.command(
    help="Show governed tags this dataset is tagged with",
)
@exception_handler("get dataset governed tags")
def governed_tags(
    ctx: typer.Context,
    dataset_id: str,
    output: OutputFormat = OutputFormatOption,
) -> None:
    callback: ClientQueryCallback[GetDatasetGovernedTags] = (
        lambda client, end_cursor: client.get_dataset_governed_tags(
            id=dataset_id, end_cursor=end_cursor
        )
    )
    nodes = list(
        paginate_query(
            ctx.obj,
            callback,
            lambda resp: (
                resp.node.governed_tags.edges
                if isinstance(resp.node, GetDatasetGovernedTagsNodeDataset)
                and resp.node.governed_tags
                else []
            ),
            lambda resp: (
                resp.node.governed_tags.page_info
                if isinstance(resp.node, GetDatasetGovernedTagsNodeDataset)
                and resp.node.governed_tags
                else GetDatasetGovernedTagsNodeDatasetGovernedTagsPageInfo(
                    hasNextPage=None, endCursor=None
                )
            ),
            edge_to_node,
        )
    )
    display_nodes(nodes, output)
