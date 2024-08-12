# Generated by ariadne-codegen

from .async_base_client import AsyncBaseClient
from .base_model import BaseModel, Upload
from .client import Client
from .enums import (
    AggregationMetadataName,
    AnchorEntityType,
    AppPlatform,
    AssetContactValueType,
    AssetEntityType,
    AssetPlatform,
    AssetRelationType,
    AssetSubType,
    BrowsePathSegmentType,
    ChangeRequestStatus,
    ChangeRequestType,
    ChartType,
    CrawlerLatestStatus,
    CrawlerType,
    CustomMetadataDataType,
    DashboardPlatform,
    DashboardType,
    DataMonitorSeverity,
    DataMonitorStatus,
    DataPlatform,
    DataQualityProvider,
    DataQualityStatus,
    DbtMaterializationType,
    DependencyCondition,
    EntityType,
    GroupPlatform,
    HierarchyType,
    InAppOnboardingCompletionStep,
    InAppProfileCompletionStep,
    InterestedPartySource,
    KnowledgeCardState,
    KnowledgeCardType,
    LineageType,
    MaterializationType,
    MetricType,
    NamespaceType,
    NativeType,
    Order,
    Persona,
    PipelineType,
    PlatformType,
    PowerBiDashboardType,
    PowerBiEndorsementType,
    PowerBiWorkspaceAccessRight,
    QueryDescriptionSupportedStatement,
    QueryDescriptionType,
    RunStatus,
    SchemaType,
    SearchContext,
    SearchIndex,
    SnowflakeStreamSourceType,
    SnowflakeStreamType,
    SystemContactSource,
    SystemTagSource,
    TenantStatus,
    ThoughtSpotDashboardType,
    ThoughtSpotDataObjectType,
    UnityCatalogDatasetType,
    UnityCatalogTableType,
    UnityCatalogVolumeType,
    UsageLevel,
    UserActivityGranularity,
    UserActivitySource,
    UserActivityType,
    UserDefinedOrderType,
    UserDefinedResourceType,
    UserRole,
    VersionUpdateField,
    VirtualViewType,
    WebhookTriggerType,
)
from .exceptions import (
    GraphQLClientError,
    GraphQLClientGraphQLError,
    GraphQLClientGraphQLMultiError,
    GraphQLClientHttpError,
    GraphQLClientInvalidResponseError,
)
from .input_types import (
    AcknowledgeChangeRequestInput,
    ActivityFeedConnectionFilterInput,
    AddTenantInput,
    AddWebhookInput,
    AISearchQueryInput,
    ApiKeyDeleteInput,
    AssetConnectionFilterInput,
    AssetContactsPatchInput,
    AssetDescriptionKnowledgeCardInput,
    AssetDescriptionTokenizedContentInput,
    AssetFilters,
    AssetGovernedTagsPatchInput,
    AssetLikeInput,
    AssetsConnectionFilterInput,
    AssetSort,
    AssociatedAssetConnectionFilterInput,
    AthenaQueryRequest,
    AuditStampInput,
    AuthorizationInput,
    AutoGeneratedDocumentInput,
    AzureAdSSOInput,
    BaseConnectionFilter,
    ChangeRequestKnowledgeCardInput,
    ChangeRequestStatusPatchInput,
    ChangeRequestTokenizedContentInput,
    ColumnDescriptionKnowledgeCardInput,
    CommentInput,
    CommentTokenizedContentInput,
    CommonColumnAttributesInput,
    CommonColumnAttributesPatchInput,
    CommonColumnDescriptionExclusionInput,
    ConnectionOrderBy,
    CrawlerFilter,
    CreateApiKeyInput,
    CreateCrawlerInput,
    CreateCrawlerScheduleInput,
    CustomMetadataConfigInput,
    CustomMetadataFacetFilterInput,
    CustomOrder,
    CustomTagAttributesInput,
    DashboardConnectionFilterInput,
    DashboardFilters,
    DashboardIdInput,
    DashboardSort,
    DataDocumentInput,
    DataDocumentTokenizedContentInput,
    DatasetColumnsInput,
    DatasetColumnsPatternInput,
    DatasetFilters,
    DatasetIdInput,
    DatasetPatternInput,
    DatasetRelationInput,
    DatasetSort,
    DbtDownstreamLineageInput,
    DbtModelRelationInput,
    DbtUpstreamLineageInput,
    DeleteCrawlerInput,
    DeleteWebhooksInput,
    DeprecationKnowledgeCardInput,
    DeprecationTokenizedContentInput,
    DesignatedContactInput,
    DropTenantInput,
    FieldTagAssociationsPatchInput,
    FieldTagPatchInput,
    FollowAssetInput,
    GeneratedAssetDescriptionInput,
    GoogleSocialLoginInput,
    GoogleWorkspaceSSOInput,
    GovernedTagFilterInput,
    GroupConnectionFilterInput,
    GroupDescriptionInput,
    GroupInfoInput,
    GroupInput,
    GroupMembersPatchInput,
    HashtagInput,
    HashtagPatchInput,
    HierarchyConnectionFilterInput,
    HierarchyFilters,
    HierarchyLogicalIdInput,
    HowToUseTokenizedContentInput,
    IncidentKnowledgeCardInput,
    IncidentTokenizedContentInput,
    InvitedPersonInput,
    KnowledgeCardAvailabilityStatusPatchInput,
    KnowledgeCardConnectionFilterInput,
    KnowledgeCardDeleteInput,
    KnowledgeCardDetailInput,
    KnowledgeCardFilters,
    KnowledgeCardIdInput,
    KnowledgeCardInfoInput,
    KnowledgeCardInput,
    KnowledgeCardSort,
    LastActiveInput,
    LDAPGroupSearchInput,
    LDAPInput,
    LDAPUserSearchInput,
    LineageFilterInput,
    LinkedInSocialLoginInput,
    MetricConnectionFilterInput,
    MetricFilters,
    MetricInfoPatchInput,
    MetricLogicalIdInput,
    MetricSort,
    MicrosoftSocialLoginInput,
    NamedAssetCollectionInput,
    NamespaceAssetsInput,
    NamespaceAssetsPatchInput,
    NamespaceAssetsUserDefinedOrderInput,
    NamespaceDeleteInput,
    NamespaceDescriptionInput,
    NamespaceFilters,
    NamespaceInfoConnectionFilterInput,
    NamespaceInfoInput,
    NamespaceInfoPatchInput,
    NamespaceInput,
    NamespaceTypeDetailInput,
    NonProdInput,
    OktaSSOInput,
    OrderedEntryInput,
    OrganizationInput,
    PersonActivityInput,
    PersonalizationOptionsInput,
    PersonalizationOptionsPatchInput,
    PersonConnectionFilterInput,
    PersonFilter,
    PersonInput,
    PersonLogicalIdInput,
    PersonOrganizationInput,
    PersonOrganizationPatchInput,
    PersonPatchInput,
    PersonPropertiesInput,
    PersonPropertiesPatchInput,
    PinOrUnpinAssetInput,
    PinsConnectionFilterInput,
    PipelineFilter,
    PowerQueryExplainerInput,
    QueryDescriptionTokenizedContentInput,
    QueryExplainerInput,
    QueryInfoConnectionFilterInput,
    QueryKnowledgeCardInput,
    QueryKnowledgeCardPatchInput,
    QueryRequest,
    RecentUserActivitiesFilterInput,
    ResourceInfoConnectionFilterInput,
    SavedLiveQueryInput,
    SearchArguments,
    SearchFacets,
    SearchQueryFilters,
    SearchQueryInput,
    SearchResultFieldsSelection,
    SearchResultSort,
    SettingsInput,
    SocialLoginInput,
    SoftDeletionInput,
    SQLExplainerInput,
    SSOInput,
    StatusBaseInput,
    SystemTagsConnectionFilterInput,
    TableauDatasourceDownstreamLineageInput,
    TableauDatasourceUpstreamLineageInput,
    ThoughtSpotDataObjectDownstreamLineageInput,
    ThoughtSpotDataObjectUpstreamLineageInput,
    UniversalSearchInput,
    UpdateApiKeyInput,
    UpdateCrawlerInput,
    UpdateCrawlerScheduleInput,
    UsageKnowledgeCardInput,
    UserDefinedResourceDeleteInput,
    UserDefinedResourceDescriptionInput,
    UserDefinedResourceFilters,
    UserDefinedResourceInfoInput,
    UserDefinedResourceInput,
    UserSpecifiedOrderingInput,
    VersionHistoryConnectionFilterInput,
    VirtualViewFilters,
    VirtualViewLogicalIdInput,
    VirtualViewSort,
)

__all__ = [
    "AISearchQueryInput",
    "AcknowledgeChangeRequestInput",
    "ActivityFeedConnectionFilterInput",
    "AddTenantInput",
    "AddWebhookInput",
    "AggregationMetadataName",
    "AnchorEntityType",
    "ApiKeyDeleteInput",
    "AppPlatform",
    "AssetConnectionFilterInput",
    "AssetContactValueType",
    "AssetContactsPatchInput",
    "AssetDescriptionKnowledgeCardInput",
    "AssetDescriptionTokenizedContentInput",
    "AssetEntityType",
    "AssetFilters",
    "AssetGovernedTagsPatchInput",
    "AssetLikeInput",
    "AssetPlatform",
    "AssetRelationType",
    "AssetSort",
    "AssetSubType",
    "AssetsConnectionFilterInput",
    "AssociatedAssetConnectionFilterInput",
    "AsyncBaseClient",
    "AthenaQueryRequest",
    "AuditStampInput",
    "AuthorizationInput",
    "AutoGeneratedDocumentInput",
    "AzureAdSSOInput",
    "BaseConnectionFilter",
    "BaseModel",
    "BrowsePathSegmentType",
    "ChangeRequestKnowledgeCardInput",
    "ChangeRequestStatus",
    "ChangeRequestStatusPatchInput",
    "ChangeRequestTokenizedContentInput",
    "ChangeRequestType",
    "ChartType",
    "Client",
    "ColumnDescriptionKnowledgeCardInput",
    "CommentInput",
    "CommentTokenizedContentInput",
    "CommonColumnAttributesInput",
    "CommonColumnAttributesPatchInput",
    "CommonColumnDescriptionExclusionInput",
    "ConnectionOrderBy",
    "CrawlerFilter",
    "CrawlerLatestStatus",
    "CrawlerType",
    "CreateApiKeyInput",
    "CreateCrawlerInput",
    "CreateCrawlerScheduleInput",
    "CustomMetadataConfigInput",
    "CustomMetadataDataType",
    "CustomMetadataFacetFilterInput",
    "CustomOrder",
    "CustomTagAttributesInput",
    "DashboardConnectionFilterInput",
    "DashboardFilters",
    "DashboardIdInput",
    "DashboardPlatform",
    "DashboardSort",
    "DashboardType",
    "DataDocumentInput",
    "DataDocumentTokenizedContentInput",
    "DataMonitorSeverity",
    "DataMonitorStatus",
    "DataPlatform",
    "DataQualityProvider",
    "DataQualityStatus",
    "DatasetColumnsInput",
    "DatasetColumnsPatternInput",
    "DatasetFilters",
    "DatasetIdInput",
    "DatasetPatternInput",
    "DatasetRelationInput",
    "DatasetSort",
    "DbtDownstreamLineageInput",
    "DbtMaterializationType",
    "DbtModelRelationInput",
    "DbtUpstreamLineageInput",
    "DeleteCrawlerInput",
    "DeleteWebhooksInput",
    "DependencyCondition",
    "DeprecationKnowledgeCardInput",
    "DeprecationTokenizedContentInput",
    "DesignatedContactInput",
    "DropTenantInput",
    "EntityType",
    "FieldTagAssociationsPatchInput",
    "FieldTagPatchInput",
    "FollowAssetInput",
    "GeneratedAssetDescriptionInput",
    "GoogleSocialLoginInput",
    "GoogleWorkspaceSSOInput",
    "GovernedTagFilterInput",
    "GraphQLClientError",
    "GraphQLClientGraphQLError",
    "GraphQLClientGraphQLMultiError",
    "GraphQLClientHttpError",
    "GraphQLClientInvalidResponseError",
    "GroupConnectionFilterInput",
    "GroupDescriptionInput",
    "GroupInfoInput",
    "GroupInput",
    "GroupMembersPatchInput",
    "GroupPlatform",
    "HashtagInput",
    "HashtagPatchInput",
    "HierarchyConnectionFilterInput",
    "HierarchyFilters",
    "HierarchyLogicalIdInput",
    "HierarchyType",
    "HowToUseTokenizedContentInput",
    "InAppOnboardingCompletionStep",
    "InAppProfileCompletionStep",
    "IncidentKnowledgeCardInput",
    "IncidentTokenizedContentInput",
    "InterestedPartySource",
    "InvitedPersonInput",
    "KnowledgeCardAvailabilityStatusPatchInput",
    "KnowledgeCardConnectionFilterInput",
    "KnowledgeCardDeleteInput",
    "KnowledgeCardDetailInput",
    "KnowledgeCardFilters",
    "KnowledgeCardIdInput",
    "KnowledgeCardInfoInput",
    "KnowledgeCardInput",
    "KnowledgeCardSort",
    "KnowledgeCardState",
    "KnowledgeCardType",
    "LDAPGroupSearchInput",
    "LDAPInput",
    "LDAPUserSearchInput",
    "LastActiveInput",
    "LineageFilterInput",
    "LineageType",
    "LinkedInSocialLoginInput",
    "MaterializationType",
    "MetricConnectionFilterInput",
    "MetricFilters",
    "MetricInfoPatchInput",
    "MetricLogicalIdInput",
    "MetricSort",
    "MetricType",
    "MicrosoftSocialLoginInput",
    "NamedAssetCollectionInput",
    "NamespaceAssetsInput",
    "NamespaceAssetsPatchInput",
    "NamespaceAssetsUserDefinedOrderInput",
    "NamespaceDeleteInput",
    "NamespaceDescriptionInput",
    "NamespaceFilters",
    "NamespaceInfoConnectionFilterInput",
    "NamespaceInfoInput",
    "NamespaceInfoPatchInput",
    "NamespaceInput",
    "NamespaceType",
    "NamespaceTypeDetailInput",
    "NativeType",
    "NonProdInput",
    "OktaSSOInput",
    "Order",
    "OrderedEntryInput",
    "OrganizationInput",
    "PersonActivityInput",
    "PersonConnectionFilterInput",
    "PersonFilter",
    "PersonInput",
    "PersonLogicalIdInput",
    "PersonOrganizationInput",
    "PersonOrganizationPatchInput",
    "PersonPatchInput",
    "PersonPropertiesInput",
    "PersonPropertiesPatchInput",
    "Persona",
    "PersonalizationOptionsInput",
    "PersonalizationOptionsPatchInput",
    "PinOrUnpinAssetInput",
    "PinsConnectionFilterInput",
    "PipelineFilter",
    "PipelineType",
    "PlatformType",
    "PowerBiDashboardType",
    "PowerBiEndorsementType",
    "PowerBiWorkspaceAccessRight",
    "PowerQueryExplainerInput",
    "QueryDescriptionSupportedStatement",
    "QueryDescriptionTokenizedContentInput",
    "QueryDescriptionType",
    "QueryExplainerInput",
    "QueryInfoConnectionFilterInput",
    "QueryKnowledgeCardInput",
    "QueryKnowledgeCardPatchInput",
    "QueryRequest",
    "RecentUserActivitiesFilterInput",
    "ResourceInfoConnectionFilterInput",
    "RunStatus",
    "SQLExplainerInput",
    "SSOInput",
    "SavedLiveQueryInput",
    "SchemaType",
    "SearchArguments",
    "SearchContext",
    "SearchFacets",
    "SearchIndex",
    "SearchQueryFilters",
    "SearchQueryInput",
    "SearchResultFieldsSelection",
    "SearchResultSort",
    "SettingsInput",
    "SnowflakeStreamSourceType",
    "SnowflakeStreamType",
    "SocialLoginInput",
    "SoftDeletionInput",
    "StatusBaseInput",
    "SystemContactSource",
    "SystemTagSource",
    "SystemTagsConnectionFilterInput",
    "TableauDatasourceDownstreamLineageInput",
    "TableauDatasourceUpstreamLineageInput",
    "TenantStatus",
    "ThoughtSpotDashboardType",
    "ThoughtSpotDataObjectDownstreamLineageInput",
    "ThoughtSpotDataObjectType",
    "ThoughtSpotDataObjectUpstreamLineageInput",
    "UnityCatalogDatasetType",
    "UnityCatalogTableType",
    "UnityCatalogVolumeType",
    "UniversalSearchInput",
    "UpdateApiKeyInput",
    "UpdateCrawlerInput",
    "UpdateCrawlerScheduleInput",
    "Upload",
    "UsageKnowledgeCardInput",
    "UsageLevel",
    "UserActivityGranularity",
    "UserActivitySource",
    "UserActivityType",
    "UserDefinedOrderType",
    "UserDefinedResourceDeleteInput",
    "UserDefinedResourceDescriptionInput",
    "UserDefinedResourceFilters",
    "UserDefinedResourceInfoInput",
    "UserDefinedResourceInput",
    "UserDefinedResourceType",
    "UserRole",
    "UserSpecifiedOrderingInput",
    "VersionHistoryConnectionFilterInput",
    "VersionUpdateField",
    "VirtualViewFilters",
    "VirtualViewLogicalIdInput",
    "VirtualViewSort",
    "VirtualViewType",
    "WebhookTriggerType",
]
