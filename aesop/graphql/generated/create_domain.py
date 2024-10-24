# Generated by ariadne-codegen
# Source: aesop/graphql/queries

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class CreateDomain(BaseModel):
    create_namespace: Optional["CreateDomainCreateNamespace"] = Field(
        alias="createNamespace"
    )


class CreateDomainCreateNamespace(BaseModel):
    id: str


CreateDomain.model_rebuild()