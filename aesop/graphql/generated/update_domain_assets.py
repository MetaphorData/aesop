# Generated by ariadne-codegen
# Source: aesop/graphql/queries

from typing import List

from pydantic import Field

from .base_model import BaseModel


class UpdateDomainAssets(BaseModel):
    update_namespace_assets: List["UpdateDomainAssetsUpdateNamespaceAssets"] = Field(
        alias="updateNamespaceAssets"
    )


class UpdateDomainAssetsUpdateNamespaceAssets(BaseModel):
    id: str


UpdateDomainAssets.model_rebuild()
