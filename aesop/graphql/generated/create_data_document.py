# Generated by ariadne-codegen
# Source: aesop/graphql/queries

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class CreateDataDocument(BaseModel):
    create_knowledge_card: Optional["CreateDataDocumentCreateKnowledgeCard"] = Field(
        alias="createKnowledgeCard"
    )


class CreateDataDocumentCreateKnowledgeCard(BaseModel):
    id: str


CreateDataDocument.model_rebuild()
