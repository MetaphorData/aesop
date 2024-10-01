from typing import Optional

from aesop.commands.aspects.user_defined_resources.tags.node import (
    GovernedTagNode,
    display_nodes,
)
from aesop.commands.common.enums.output_format import OutputFormat
from aesop.commands.common.paginator import ClientQueryCallback, paginate_query
from aesop.config import AesopConfig
from aesop.graphql.generated.get_governed_tags import (
    GetGovernedTags,
    GetGovernedTagsUserDefinedResourcesEdges,
)


def edge_to_node(
    edge: GetGovernedTagsUserDefinedResourcesEdges,
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


def get(
    name: Optional[str],
    output: OutputFormat,
    config: AesopConfig,
) -> None:
    callback: ClientQueryCallback[GetGovernedTags] = (
        lambda client, end_cursor: client.get_governed_tags(
            name=name, end_cursor=end_cursor
        )
    )

    nodes = list(
        paginate_query(
            config,
            callback,
            lambda resp: resp.user_defined_resources.edges,
            lambda resp: resp.user_defined_resources.page_info,
            edge_to_node,
        )
    )
    display_nodes(nodes, output)
