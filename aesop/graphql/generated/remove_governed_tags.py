# Generated by ariadne-codegen
# Source: aesop/graphql/queries

from typing import List

from pydantic import Field

from .base_model import BaseModel


class RemoveGovernedTags(BaseModel):
    delete_user_defined_resource: "RemoveGovernedTagsDeleteUserDefinedResource" = Field(
        alias="deleteUserDefinedResource"
    )


class RemoveGovernedTagsDeleteUserDefinedResource(BaseModel):
    deleted_ids: List[str] = Field(alias="deletedIds")
    failed_ids: List[str] = Field(alias="failedIds")


RemoveGovernedTags.model_rebuild()
