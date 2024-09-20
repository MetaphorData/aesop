# Generated by ariadne-codegen
# Source: aesop/graphql/queries

from typing import List

from pydantic import Field

from .base_model import BaseModel


class GetSetupInfo(BaseModel):
    setup_info: "GetSetupInfoSetupInfo" = Field(alias="setupInfo")


class GetSetupInfoSetupInfo(BaseModel):
    oidc: "GetSetupInfoSetupInfoOidc"
    saml: "GetSetupInfoSetupInfoSaml"
    crawler_ip_addresses: List[str] = Field(alias="crawlerIpAddresses")


class GetSetupInfoSetupInfoOidc(BaseModel):
    sign_in_redirect_url: str = Field(alias="signInRedirectUrl")


class GetSetupInfoSetupInfoSaml(BaseModel):
    entity_id: str = Field(alias="entityId")
    reply_acs_url: str = Field(alias="replyACSUrl")
    sign_on_url: str = Field(alias="signOnUrl")


GetSetupInfo.model_rebuild()
GetSetupInfoSetupInfo.model_rebuild()
