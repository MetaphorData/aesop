from typing import List, Optional

from rich import print
from typer import Context, Typer

from aesop.commands.common.exception_handler import exception_handler
from aesop.commands.common.paginator import ClientQueryCallback, paginate_query
from aesop.config import AesopConfig
from aesop.graphql.generated.get_domain_assets import (
    GetDomainAssets,
    GetDomainAssetsNodeNamespace,
    GetDomainAssetsNodeNamespaceNamespaceAssetsAssetsEdges,
    GetDomainAssetsNodeNamespaceNamespaceAssetsAssetsEdgesNode,
    GetDomainAssetsNodeNamespaceNamespaceAssetsAssetsPageInfo,
)

app = Typer(help="Manages assets in a Metaphor data domain.")


@exception_handler("add domain asset")
@app.command(help="Adds an asset to a data domain.")
def add(
    ctx: Context,
    domain_id: str,
    asset_id: str,
    collection_name: Optional[str] = None,
) -> None:
    config: AesopConfig = ctx.obj
    client = config.get_graphql_client()
    client.update_domain_assets(
        id=domain_id,
        asset_ids_to_add=[asset_id],
        collection_name=collection_name,
        remove_collection=False,
    )
    print(
        f"Added asset id {asset_id} to {domain_id}"
        + (f", collection name = {collection_name}" if collection_name else "")
    )


@exception_handler("get domain assets")
@app.command(help="Gets the ids of the assets that belong to the data domain.")
def get(
    ctx: Context,
    domain_id: str,
) -> None:
    config: AesopConfig = ctx.obj
    callback: ClientQueryCallback[GetDomainAssets] = (
        lambda client, end_cursor: client.get_domain_assets(domain_id, end_cursor)
    )

    def edges_projection(
        resp: GetDomainAssets,
    ) -> List[Optional[GetDomainAssetsNodeNamespaceNamespaceAssetsAssetsEdges]]:
        if (
            resp.node
            and isinstance(resp.node, GetDomainAssetsNodeNamespace)
            and resp.node.namespace_assets
            and resp.node.namespace_assets.assets
        ):
            return resp.node.namespace_assets.assets.edges
        return []

    def page_info_projection(
        resp: GetDomainAssets,
    ) -> GetDomainAssetsNodeNamespaceNamespaceAssetsAssetsPageInfo:
        if (
            resp.node
            and isinstance(resp.node, GetDomainAssetsNodeNamespace)
            and resp.node.namespace_assets
            and resp.node.namespace_assets.assets
        ):
            return resp.node.namespace_assets.assets.page_info
        return GetDomainAssetsNodeNamespaceNamespaceAssetsAssetsPageInfo(
            hasNextPage=False, endCursor=None
        )

    # Need this for mypy to work
    def edge_to_node(
        edge: GetDomainAssetsNodeNamespaceNamespaceAssetsAssetsEdges,
    ) -> GetDomainAssetsNodeNamespaceNamespaceAssetsAssetsEdgesNode:
        return edge.node

    asset_ids = [
        x.id
        for x in paginate_query(
            config, callback, edges_projection, page_info_projection, edge_to_node
        )
    ]
    print(asset_ids)


@exception_handler("remove domain asset")
@app.command(help="Removes an asset from the data domain.")
def remove(
    ctx: Context,
    domain_id: str,
    asset_id: str,
    collection_name: Optional[str] = None,
) -> None:
    config: AesopConfig = ctx.obj
    client = config.get_graphql_client()
    client.update_domain_assets(
        id=domain_id,
        asset_ids_to_remove=[asset_id],
        collection_name=collection_name,
        remove_collection=False,
    )
    print(
        f"Removed asset id {asset_id} from {domain_id}"
        + (f", collection name = {collection_name}" if collection_name else "")
    )


@exception_handler("remove named asset collection")
@app.command(help="Removes a named asset collection from the data domain.")
def remove_collection(
    ctx: Context,
    domain_id: str,
    collection_name: str,
) -> None:
    config: AesopConfig = ctx.obj
    client = config.get_graphql_client()
    client.update_domain_assets(
        id=domain_id,
        collection_name=collection_name,
        remove_collection=True,
    )
    print(f"Removed named asset collection {collection_name} from {domain_id}")
