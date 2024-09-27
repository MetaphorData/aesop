# Generated by ariadne-codegen
# Source: aesop/graphql/queries

from typing import List, Literal

from pydantic import Field

from .base_model import BaseModel


class UnassignGovernedTags(BaseModel):
    upsert_asset_governed_tags: List["UnassignGovernedTagsUpsertAssetGovernedTags"] = (
        Field(alias="upsertAssetGovernedTags")
    )


class UnassignGovernedTagsUpsertAssetGovernedTags(BaseModel):
    typename__: Literal[
        "Dashboard",
        "Dataset",
        "Entity",
        "Group",
        "Hierarchy",
        "KnowledgeCard",
        "Metric",
        "Namespace",
        "Person",
        "Pipeline",
        "UserDefinedResource",
        "VirtualView",
    ] = Field(alias="__typename")
    id: str


UnassignGovernedTags.model_rebuild()
