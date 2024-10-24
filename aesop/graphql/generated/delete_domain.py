# Generated by ariadne-codegen
# Source: aesop/graphql/queries

from typing import List

from pydantic import Field

from .base_model import BaseModel


class DeleteDomain(BaseModel):
    delete_namespaces: "DeleteDomainDeleteNamespaces" = Field(alias="deleteNamespaces")


class DeleteDomainDeleteNamespaces(BaseModel):
    deleted_ids: List[str] = Field(alias="deletedIds")
    failed_ids: List[str] = Field(alias="failedIds")


DeleteDomain.model_rebuild()
