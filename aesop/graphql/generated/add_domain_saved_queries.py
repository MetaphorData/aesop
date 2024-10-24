# Generated by ariadne-codegen
# Source: aesop/graphql/queries

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class AddDomainSavedQueries(BaseModel):
    update_namespace_info: Optional["AddDomainSavedQueriesUpdateNamespaceInfo"] = Field(
        alias="updateNamespaceInfo"
    )


class AddDomainSavedQueriesUpdateNamespaceInfo(BaseModel):
    id: str


AddDomainSavedQueries.model_rebuild()
