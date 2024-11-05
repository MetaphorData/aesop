import json
from typing import List, Optional

from rich import print
from typer import Context, Typer

from aesop.commands.common.exception_handler import exception_handler
from aesop.config import AesopConfig
from aesop.graphql.generated.enums import SearchContext
from aesop.graphql.generated.fragments import (
    NamespacePartsNamespaceInfoDetailSavedQueries,
)
from aesop.graphql.generated.get_domain import GetDomainNodeNamespace
from aesop.graphql.generated.input_types import (
    CustomAttributesInput,
    SavedLiveQueryInput,
)

app = Typer(help="Manages saved live queries for Metaphor data domains.")


@exception_handler("add saved query")
@app.command(help="Adds a live query to a Metaphor data domain.")
def add(
    ctx: Context,
    domain_id: str,
    search_context: Optional[SearchContext] = None,
    facets_json: Optional[str] = None,
    keyword: Optional[str] = None,
    name: Optional[str] = None,
) -> None:
    if not facets_json and not keyword:
        raise ValueError("Must specify either `facets_json` or `keyword`")
    if facets_json:
        try:
            json.loads(facets_json)
        except Exception:
            raise ValueError(
                f"Invalid facets_json, must be a valid JSON value: {facets_json}"
            )

    config: AesopConfig = ctx.obj
    client = config.get_graphql_client()
    domain = client.get_domain(domain_id).node
    if not domain:
        raise ValueError(f"Cannot find domain: {domain_id}")

    assert isinstance(domain, GetDomainNodeNamespace) and domain.namespace_info
    namespace_info = domain.namespace_info
    saved_queries_input = [
        SavedLiveQueryInput(
            context=q.context,
            facetsJSON=q.facets_json,
            keyword=q.keyword,
            name=q.name,
        )
        for q in namespace_info.detail.saved_queries or []
    ]
    saved_queries_input.append(
        SavedLiveQueryInput(
            context=search_context,
            facetsJSON=facets_json,
            keyword=keyword,
            name=name,
        )
    )
    resp = (
        config.get_graphql_client()
        .update_domain_saved_queries(
            id=domain_id,
            saved_queries=saved_queries_input,
            name=namespace_info.name,
            visible_to=namespace_info.visible_to,
            custom_attributes=(
                CustomAttributesInput(
                    color=namespace_info.custom_attributes.color,
                    iconKey=namespace_info.custom_attributes.icon_key,
                )
                if namespace_info.custom_attributes
                else None
            ),
            parent_id=domain.parent_namespace.id if domain.parent_namespace else None,
        )
        .update_namespace_info
    )
    assert resp
    print(f"Added saved query to {resp.id}")


@exception_handler("remove saved query")
@app.command(help="Removes a saved live query from a Metaphor data domain.")
def remove(
    ctx: Context,
    domain_id: str,
    saved_query_id: Optional[str] = None,
    saved_query_name: Optional[str] = None,
) -> None:
    config: AesopConfig = ctx.obj
    client = config.get_graphql_client()
    domain = client.get_domain(domain_id).node
    if not domain:
        raise ValueError(f"Cannot find domain: {id}")

    if (saved_query_id is not None) == (saved_query_name is not None):
        raise ValueError(
            "Only one of `saved_query_name` or `saved_query_id` should be specified"
        )

    assert isinstance(domain, GetDomainNodeNamespace) and domain.namespace_info
    namespace_info = domain.namespace_info
    saved_queries = namespace_info.detail.saved_queries or []

    def should_include(
        q: NamespacePartsNamespaceInfoDetailSavedQueries,
    ) -> bool:
        if saved_query_id:
            return q.id != saved_query_id
        return q.name != saved_query_name

    saved_queries_input: List[SavedLiveQueryInput] = []
    need_to_remove = False
    for q in saved_queries:
        if should_include(q):
            saved_queries_input.append(
                SavedLiveQueryInput(
                    context=q.context,
                    facetsJSON=q.facets_json,
                    keyword=q.keyword,
                    name=q.name,
                )
            )
        else:
            # Found the saved query to remove
            need_to_remove = True

    if not need_to_remove:
        # Nothing to do
        return

    resp = (
        config.get_graphql_client()
        .update_domain_saved_queries(
            id=domain_id,
            saved_queries=saved_queries_input,
            name=namespace_info.name,
            visible_to=namespace_info.visible_to,
            custom_attributes=(
                CustomAttributesInput(
                    color=namespace_info.custom_attributes.color,
                    iconKey=namespace_info.custom_attributes.icon_key,
                )
                if namespace_info.custom_attributes
                else None
            ),
            parent_id=domain.parent_namespace.id if domain.parent_namespace else None,
        )
        .update_namespace_info
    )
    assert resp
    print(f"Removed saved query from {resp.id}")
