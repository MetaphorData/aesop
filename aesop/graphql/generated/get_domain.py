# Generated by ariadne-codegen
# Source: aesop/graphql/queries

from typing import Annotated, Any, List, Literal, Optional, Union

from pydantic import Field

from .base_model import BaseModel
from .enums import SearchContext


class GetDomain(BaseModel):
    node: Optional[
        Annotated[
            Union["GetDomainNodeNode", "GetDomainNodeNamespace"],
            Field(discriminator="typename__"),
        ]
    ]


class GetDomainNodeNode(BaseModel):
    typename__: Literal[
        "API",
        "Crawler",
        "CrawlerRun",
        "Dashboard",
        "Dataset",
        "Group",
        "Hierarchy",
        "KnowledgeCard",
        "Metric",
        "Node",
        "Person",
        "Pipeline",
        "SystemTagCounts",
        "UserDefinedResource",
        "VirtualView",
    ] = Field(alias="__typename")


class GetDomainNodeNamespace(BaseModel):
    typename__: Literal["Namespace"] = Field(alias="__typename")
    namespace_info: Optional["GetDomainNodeNamespaceNamespaceInfo"] = Field(
        alias="namespaceInfo"
    )
    parent_namespace: Optional["GetDomainNodeNamespaceParentNamespace"] = Field(
        alias="parentNamespace"
    )
    namespace_assets: Optional["GetDomainNodeNamespaceNamespaceAssets"] = Field(
        alias="namespaceAssets"
    )


class GetDomainNodeNamespaceNamespaceInfo(BaseModel):
    name: str
    created: "GetDomainNodeNamespaceNamespaceInfoCreated"
    last_modified: "GetDomainNodeNamespaceNamespaceInfoLastModified" = Field(
        alias="lastModified"
    )
    detail: "GetDomainNodeNamespaceNamespaceInfoDetail"
    visible_to: List[str] = Field(alias="visibleTo")
    description: Optional["GetDomainNodeNamespaceNamespaceInfoDescription"]
    custom_attributes: Optional[
        "GetDomainNodeNamespaceNamespaceInfoCustomAttributes"
    ] = Field(alias="customAttributes")


class GetDomainNodeNamespaceNamespaceInfoCreated(BaseModel):
    time: Any
    actor: Optional[str]


class GetDomainNodeNamespaceNamespaceInfoLastModified(BaseModel):
    time: Any
    actor: Optional[str]


class GetDomainNodeNamespaceNamespaceInfoDetail(BaseModel):
    saved_queries: Optional[
        List["GetDomainNodeNamespaceNamespaceInfoDetailSavedQueries"]
    ] = Field(alias="savedQueries")


class GetDomainNodeNamespaceNamespaceInfoDetailSavedQueries(BaseModel):
    name: Optional[str]
    keyword: str
    context: Optional[SearchContext]
    id: str
    facets_json: Optional[str] = Field(alias="facetsJSON")


class GetDomainNodeNamespaceNamespaceInfoDescription(BaseModel):
    text: Optional[str]
    tokenized_text: Optional[str] = Field(alias="tokenizedText")


class GetDomainNodeNamespaceNamespaceInfoCustomAttributes(BaseModel):
    color: Optional[str]
    icon_key: Optional[str] = Field(alias="iconKey")


class GetDomainNodeNamespaceParentNamespace(BaseModel):
    id: str


class GetDomainNodeNamespaceNamespaceAssets(BaseModel):
    named_asset_collections: Optional[
        List["GetDomainNodeNamespaceNamespaceAssetsNamedAssetCollections"]
    ] = Field(alias="namedAssetCollections")


class GetDomainNodeNamespaceNamespaceAssetsNamedAssetCollections(BaseModel):
    name: str
    asset_ids: List[str] = Field(alias="assetIds")


GetDomain.model_rebuild()
GetDomainNodeNamespace.model_rebuild()
GetDomainNodeNamespaceNamespaceInfo.model_rebuild()
GetDomainNodeNamespaceNamespaceInfoDetail.model_rebuild()
GetDomainNodeNamespaceNamespaceAssets.model_rebuild()
