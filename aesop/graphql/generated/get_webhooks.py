# Generated by ariadne-codegen
# Source: aesop/graphql/queries

from typing import List

from pydantic import Field

from .base_model import BaseModel


class GetWebhooks(BaseModel):
    webhooks: List["GetWebhooksWebhooks"]


class GetWebhooksWebhooks(BaseModel):
    id: str = Field(alias="_id")


GetWebhooks.model_rebuild()
