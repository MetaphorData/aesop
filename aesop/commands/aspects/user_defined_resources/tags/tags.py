from enum import Enum
from typing import List, Optional

import typer

from aesop.commands.aspects.user_defined_resources.tags.models import (
    AddTagsOutput,
    BatchAddTagsInput,
    BatchAssignTagsInput,
    BatchRemoveTagsInput,
    GovernedTag,
    RemoveTagsOutput,
)
from aesop.commands.aspects.user_defined_resources.tags.node import (
    GovernedTagNode,
    display_nodes,
)
from aesop.commands.common.arguments import InputFileArg
from aesop.commands.common.enums.output_format import OutputFormat
from aesop.commands.common.exception_handler import exception_handler
from aesop.commands.common.options import OutputFormatOption
from aesop.commands.common.paginator import ClientQueryCallback, paginate_query
from aesop.config import AesopConfig
from aesop.console import console
from aesop.graphql.generated.get_governed_tag import (
    GetGovernedTagNodeUserDefinedResource,
)
from aesop.graphql.generated.get_governed_tag_child_tags import GetGovernedTagChildTags
from aesop.graphql.generated.get_governed_tag_child_tags import (
    GetGovernedTagChildTagsNodeUserDefinedResource as GetChildTags,
)
from aesop.graphql.generated.get_governed_tag_child_tags import (
    GetGovernedTagChildTagsNodeUserDefinedResourceChildResourcesEdges as GetChildTagsEdge,
)
from aesop.graphql.generated.get_governed_tag_child_tags import (
    GetGovernedTagChildTagsNodeUserDefinedResourceChildResourcesPageInfo as GetChildTagsPageInfo,
)
from aesop.graphql.generated.input_types import CustomTagAttributesInput
from aesop.graphql.generated.list_governed_tags import (
    ListGovernedTagsUserDefinedResourcesEdges,
)

from .commands.add import add_tags
from .commands.assign import assign_tags
from .commands.remove import remove_tags
from .commands.unassign import unassign_tags

app = typer.Typer(help="Manage tags in Metaphor.")


class TagsRichPanelNames(str, Enum):
    add = "Adding tags"
    assign = "Assigning tags"
    get = "Getting tag"
    list = "Listing tags"
    remove = "Removing tags"
    unassign = "Unassigning tags"


@app.command(
    help="Add a single governed tag with optional description text to Metaphor.",
    rich_help_panel=TagsRichPanelNames.add,
)
@exception_handler("add tag")
def add(
    ctx: typer.Context,
    name: str,
    description: Optional[str] = None,
    parent_id: Optional[str] = None,
    color: Optional[str] = None,
    icon_key: Optional[str] = None,
    output: OutputFormat = OutputFormatOption,
) -> None:
    custom_attributes = (
        CustomTagAttributesInput(color=color, iconKey=icon_key)
        if color or icon_key
        else None
    )
    tag = GovernedTag(
        name=name,
        description=description,
        parent_id=parent_id,
        custom_attributes=custom_attributes,
    )
    created_ids = add_tags([tag], ctx.obj)
    AddTagsOutput(created_ids=created_ids).display(output)


@app.command(
    help="Batch add governed tags with optional description text to Metaphor.",
    rich_help_panel=TagsRichPanelNames.add,
)
@exception_handler("batch add tags")
def batch_add(
    ctx: typer.Context,
    input_file: typer.FileText = InputFileArg(BatchAddTagsInput),
    output: OutputFormat = OutputFormatOption,
) -> None:
    batch_add_tags_input = BatchAddTagsInput.model_validate_json(input_file.read())
    created_ids = add_tags(batch_add_tags_input.tags, ctx.obj)
    AddTagsOutput(created_ids=created_ids).display(output)


@app.command(
    help="Assign a governed tag to an asset.",
    rich_help_panel=TagsRichPanelNames.assign,
)
@exception_handler("assign tag")
def assign(
    ctx: typer.Context,
    tag_id: str,
    asset_id: str,
) -> None:
    ids = assign_tags([tag_id], [asset_id], ctx.obj)
    console.ok(f"Assigned governed tag {tag_id} to asset {ids[0]}")


@app.command(
    help="Batch assign governed tags to multiple assets",
    rich_help_panel=TagsRichPanelNames.assign,
)
@exception_handler("batch assign tags")
def batch_assign(
    ctx: typer.Context,
    input_file: typer.FileText = InputFileArg(BatchAssignTagsInput),
) -> None:
    input = BatchAssignTagsInput.model_validate_json(input_file.read())
    ids = assign_tags(input.tag_ids, input.asset_ids, ctx.obj)
    console.ok(f"Assigned governed tags {input.tag_ids} to assets {ids}")


@exception_handler("get tag")
@app.command(
    help="Get governed tag",
    rich_help_panel=TagsRichPanelNames.get,
)
def get(
    ctx: typer.Context,
    id: str,
    output: OutputFormat = OutputFormatOption,
) -> None:
    config: AesopConfig = ctx.obj
    resp = config.get_graphql_client().get_governed_tag(id).node
    if not resp:
        return
    assert isinstance(resp, GetGovernedTagNodeUserDefinedResource)
    node = GovernedTagNode.from_gql_response(resp)
    if node:
        display_nodes([node], output)


@exception_handler("get child tags")
@app.command(
    help="Get the child tags of a governed tag",
    rich_help_panel=TagsRichPanelNames.list,
)
def get_child_tags(
    ctx: typer.Context,
    id: str,
    output: OutputFormat = OutputFormatOption,
) -> None:
    def edge_to_node(edge: GetChildTagsEdge) -> Optional[GovernedTagNode]:
        return GovernedTagNode.from_gql_response(edge.node)

    config: AesopConfig = ctx.obj
    callback: ClientQueryCallback[GetGovernedTagChildTags] = (
        lambda client, end_cursor: client.get_governed_tag_child_tags(id, end_cursor)
    )

    def edge_projection(
        resp: GetGovernedTagChildTags,
    ) -> List[Optional[GetChildTagsEdge]]:
        if isinstance(resp.node, GetChildTags):
            return resp.node.child_resources.edges
        return []

    def page_info_projection(resp: GetGovernedTagChildTags) -> GetChildTagsPageInfo:
        if isinstance(resp.node, GetChildTags):
            return resp.node.child_resources.page_info
        return GetChildTagsPageInfo(hasNextPage=False, endCursor=None)

    nodes = list(
        paginate_query(
            config,
            callback,
            edge_projection,
            page_info_projection,
            edge_to_node,
        )
    )
    display_nodes(nodes, output)


@app.command(
    help="list governed tags.",
    rich_help_panel=TagsRichPanelNames.list,
    name="list",
)
@exception_handler("list tags")
def list_governed_tags(
    ctx: typer.Context,
    name: Optional[str] = typer.Option(
        default=None,
        help="Filter for the name of the governed tag",
    ),
    output: OutputFormat = OutputFormatOption,
) -> None:
    def edge_to_node(
        edge: ListGovernedTagsUserDefinedResourcesEdges,
    ) -> Optional[GovernedTagNode]:
        return GovernedTagNode.from_gql_response(edge.node)

    config: AesopConfig = ctx.obj

    nodes = list(
        paginate_query(
            config,
            lambda client, end_cursor: client.list_governed_tags(name, end_cursor),
            lambda resp: resp.user_defined_resources.edges,
            lambda resp: resp.user_defined_resources.page_info,
            edge_to_node,
        )
    )
    display_nodes(nodes, output)


@app.command(
    help="Remove a governed tag from Metaphor.",
    rich_help_panel=TagsRichPanelNames.remove,
)
@exception_handler("remove tag")
def remove(
    tag_id: str,
    ctx: typer.Context,
    output: OutputFormat = OutputFormatOption,
) -> None:
    resp = remove_tags([tag_id], ctx.obj)
    RemoveTagsOutput(
        removed_ids=resp.delete_user_defined_resource.deleted_ids,
        failed_ids=resp.delete_user_defined_resource.failed_ids,
    ).display(output)


@app.command(
    help="Batch remove governed tags from Metaphor.",
    rich_help_panel=TagsRichPanelNames.remove,
)
@exception_handler("batch remove tags")
def batch_remove(
    ctx: typer.Context,
    input_file: typer.FileText = InputFileArg(BatchRemoveTagsInput),
    output: OutputFormat = OutputFormatOption,
) -> None:
    input = BatchRemoveTagsInput.model_validate_json(input_file.read())
    resp = remove_tags(input.tag_ids, ctx.obj)
    RemoveTagsOutput(
        removed_ids=resp.delete_user_defined_resource.deleted_ids,
        failed_ids=resp.delete_user_defined_resource.failed_ids,
    ).display(output)


@app.command(
    help="Unassign a governed tag from an asset.",
    rich_help_panel=TagsRichPanelNames.unassign,
)
@exception_handler("unassign tag")
def unassign(
    ctx: typer.Context,
    tag_id: str,
    asset_id: str,
) -> None:
    ids = unassign_tags([tag_id], [asset_id], ctx.obj)
    console.ok(f"Unassigned governed tag {tag_id} from asset {ids[0]}")


@app.command(
    help="Unassign governed tags from assets.",
    rich_help_panel=TagsRichPanelNames.unassign,
)
@exception_handler("batch unassign tags")
def batch_unassign(
    ctx: typer.Context,
    input_file: typer.FileText = InputFileArg(BatchAssignTagsInput),
) -> None:
    input = BatchAssignTagsInput.model_validate_json(input_file.read())
    ids = unassign_tags(input.tag_ids, input.asset_ids, ctx.obj)
    console.ok(f"Unassigned governed tags {input.tag_ids} from assets {ids}")
