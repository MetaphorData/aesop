# Generated by ariadne-codegen
# Source: aesop/graphql/queries

from typing import Any, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import ChangeRequestStatus, KnowledgeCardType


class CreateKnowledgeCard(BaseModel):
    create_knowledge_card: Optional["CreateKnowledgeCardCreateKnowledgeCard"] = Field(
        alias="createKnowledgeCard"
    )


class CreateKnowledgeCardCreateKnowledgeCard(BaseModel):
    knowledge_card_info: Optional[
        "CreateKnowledgeCardCreateKnowledgeCardKnowledgeCardInfo"
    ] = Field(alias="knowledgeCardInfo")


class CreateKnowledgeCardCreateKnowledgeCardKnowledgeCardInfo(BaseModel):
    detail: "CreateKnowledgeCardCreateKnowledgeCardKnowledgeCardInfoDetail"


class CreateKnowledgeCardCreateKnowledgeCardKnowledgeCardInfoDetail(BaseModel):
    type: KnowledgeCardType
    change_request: Optional[
        "CreateKnowledgeCardCreateKnowledgeCardKnowledgeCardInfoDetailChangeRequest"
    ] = Field(alias="changeRequest")


class CreateKnowledgeCardCreateKnowledgeCardKnowledgeCardInfoDetailChangeRequest(
    BaseModel
):
    status: Optional[
        "CreateKnowledgeCardCreateKnowledgeCardKnowledgeCardInfoDetailChangeRequestStatus"
    ]


class CreateKnowledgeCardCreateKnowledgeCardKnowledgeCardInfoDetailChangeRequestStatus(
    BaseModel
):
    status: Optional[ChangeRequestStatus]
    last_modified: (
        "CreateKnowledgeCardCreateKnowledgeCardKnowledgeCardInfoDetailChangeRequestStatusLastModified"
    ) = Field(alias="lastModified")
    created: "CreateKnowledgeCardCreateKnowledgeCardKnowledgeCardInfoDetailChangeRequestStatusCreated"


class CreateKnowledgeCardCreateKnowledgeCardKnowledgeCardInfoDetailChangeRequestStatusLastModified(
    BaseModel
):
    time: Any
    acting_person: Optional[
        "CreateKnowledgeCardCreateKnowledgeCardKnowledgeCardInfoDetailChangeRequestStatusLastModifiedActingPerson"
    ] = Field(alias="actingPerson")


class CreateKnowledgeCardCreateKnowledgeCardKnowledgeCardInfoDetailChangeRequestStatusLastModifiedActingPerson(
    BaseModel
):
    properties: Optional[
        "CreateKnowledgeCardCreateKnowledgeCardKnowledgeCardInfoDetailChangeRequestStatusLastModifiedActingPersonProperties"
    ]


class CreateKnowledgeCardCreateKnowledgeCardKnowledgeCardInfoDetailChangeRequestStatusLastModifiedActingPersonProperties(
    BaseModel
):
    first_name: str = Field(alias="firstName")


class CreateKnowledgeCardCreateKnowledgeCardKnowledgeCardInfoDetailChangeRequestStatusCreated(
    BaseModel
):
    time: Any
    acting_person: Optional[
        "CreateKnowledgeCardCreateKnowledgeCardKnowledgeCardInfoDetailChangeRequestStatusCreatedActingPerson"
    ] = Field(alias="actingPerson")


class CreateKnowledgeCardCreateKnowledgeCardKnowledgeCardInfoDetailChangeRequestStatusCreatedActingPerson(
    BaseModel
):
    properties: Optional[
        "CreateKnowledgeCardCreateKnowledgeCardKnowledgeCardInfoDetailChangeRequestStatusCreatedActingPersonProperties"
    ]


class CreateKnowledgeCardCreateKnowledgeCardKnowledgeCardInfoDetailChangeRequestStatusCreatedActingPersonProperties(
    BaseModel
):
    first_name: str = Field(alias="firstName")


CreateKnowledgeCard.model_rebuild()
CreateKnowledgeCardCreateKnowledgeCard.model_rebuild()
CreateKnowledgeCardCreateKnowledgeCardKnowledgeCardInfo.model_rebuild()
CreateKnowledgeCardCreateKnowledgeCardKnowledgeCardInfoDetail.model_rebuild()
CreateKnowledgeCardCreateKnowledgeCardKnowledgeCardInfoDetailChangeRequest.model_rebuild()
CreateKnowledgeCardCreateKnowledgeCardKnowledgeCardInfoDetailChangeRequestStatus.model_rebuild()
CreateKnowledgeCardCreateKnowledgeCardKnowledgeCardInfoDetailChangeRequestStatusLastModified.model_rebuild()
CreateKnowledgeCardCreateKnowledgeCardKnowledgeCardInfoDetailChangeRequestStatusLastModifiedActingPerson.model_rebuild()
CreateKnowledgeCardCreateKnowledgeCardKnowledgeCardInfoDetailChangeRequestStatusCreated.model_rebuild()
CreateKnowledgeCardCreateKnowledgeCardKnowledgeCardInfoDetailChangeRequestStatusCreatedActingPerson.model_rebuild()
