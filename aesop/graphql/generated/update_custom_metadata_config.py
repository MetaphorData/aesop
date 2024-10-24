# Generated by ariadne-codegen
# Source: aesop/graphql/queries

from typing import Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import CustomMetadataDataType


class UpdateCustomMetadataConfig(BaseModel):
    update_custom_metadata_config: (
        "UpdateCustomMetadataConfigUpdateCustomMetadataConfig"
    ) = Field(alias="updateCustomMetadataConfig")


class UpdateCustomMetadataConfigUpdateCustomMetadataConfig(BaseModel):
    key: str
    display_name: Optional[str] = Field(alias="displayName")
    data_type: CustomMetadataDataType = Field(alias="dataType")
    searchable: Optional[bool]
    highlight: Optional[bool]
    searchable: Optional[bool]


UpdateCustomMetadataConfig.model_rebuild()