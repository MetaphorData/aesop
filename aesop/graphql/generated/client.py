# Generated by ariadne-codegen
# Source: aesop/graphql/queries

from typing import Any, Dict, List, Optional, Union

from .add_governed_tags import AddGovernedTags
from .add_webhook import AddWebhook
from .assign_governed_tags import AssignGovernedTags
from .attach_data_documents_to_namespace import AttachDataDocumentsToNamespace
from .base_client import BaseClient
from .base_model import UNSET, UnsetType
from .create_data_document import CreateDataDocument
from .create_domain import CreateDomain
from .create_knowledge_card import CreateKnowledgeCard
from .create_namespace import CreateNamespace
from .delete_data_document import DeleteDataDocument
from .delete_domain import DeleteDomain
from .enums import NamespaceType, WebhookTriggerType
from .get_custom_metadata_settings import GetCustomMetadataSettings
from .get_data_document import GetDataDocument
from .get_dataset_governed_tags import GetDatasetGovernedTags
from .get_domain import GetDomain
from .get_domain_assets import GetDomainAssets
from .get_governed_tag import GetGovernedTag
from .get_governed_tag_child_tags import GetGovernedTagChildTags
from .get_namespaces import GetNamespaces
from .get_non_prod_settings import GetNonProdSettings
from .get_setup_info import GetSetupInfo
from .get_soft_deletion_settings import GetSoftDeletionSettings
from .get_user import GetUser
from .get_webhook_payload_schema import GetWebhookPayloadSchema
from .get_webhooks import GetWebhooks
from .input_types import (
    AssetGovernedTagsPatchInput,
    CustomAttributesInput,
    HashtagInput,
    KnowledgeCardInput,
    NamespaceDescriptionInput,
    SavedLiveQueryInput,
    SettingsInput,
    UpdateCustomMetadataConfigInput,
    UserDefinedResourceDeleteInput,
    UserDefinedResourceInput,
)
from .list_governed_tags import ListGovernedTags
from .remove_governed_tags import RemoveGovernedTags
from .remove_webhook import RemoveWebhook
from .unassign_governed_tags import UnassignGovernedTags
from .update_custom_metadata_config import UpdateCustomMetadataConfig
from .update_domain_assets import UpdateDomainAssets
from .update_domain_info import UpdateDomainInfo
from .update_domain_saved_queries import UpdateDomainSavedQueries
from .update_settings import UpdateSettings


def gql(q: str) -> str:
    return q


class Client(BaseClient):
    def create_knowledge_card(
        self, data: KnowledgeCardInput, **kwargs: Any
    ) -> CreateKnowledgeCard:
        query = gql(
            """
            mutation createKnowledgeCard($data: KnowledgeCardInput!) {
              createKnowledgeCard(data: $data) {
                knowledgeCardInfo {
                  detail {
                    type
                    changeRequest {
                      status {
                        status
                        lastModified {
                          time
                          actingPerson {
                            properties {
                              firstName
                            }
                          }
                        }
                        created {
                          time
                          actingPerson {
                            properties {
                              firstName
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"data": data}
        response = self.execute(
            query=query,
            operation_name="createKnowledgeCard",
            variables=variables,
            **kwargs
        )
        _data = self.get_data(response)
        return CreateKnowledgeCard.model_validate(_data)

    def attach_data_documents_to_namespace(
        self, namespace_id: str, data_document_ids: List[str], **kwargs: Any
    ) -> AttachDataDocumentsToNamespace:
        query = gql(
            """
            mutation attachDataDocumentsToNamespace($namespaceId: ID!, $dataDocumentIds: [ID!]!) {
              updateNamespaceAssets(
                input: {entityIds: [$namespaceId], assetIdsToAdd: $dataDocumentIds}
              ) {
                id
              }
            }
            """
        )
        variables: Dict[str, object] = {
            "namespaceId": namespace_id,
            "dataDocumentIds": data_document_ids,
        }
        response = self.execute(
            query=query,
            operation_name="attachDataDocumentsToNamespace",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return AttachDataDocumentsToNamespace.model_validate(data)

    def create_data_document(
        self,
        name: str,
        content: str,
        publish: bool,
        hashtags: Union[Optional[List[HashtagInput]], UnsetType] = UNSET,
        impersonated_as: Union[Optional[str], UnsetType] = UNSET,
        **kwargs: Any
    ) -> CreateDataDocument:
        query = gql(
            """
            mutation createDataDocument($name: String!, $content: String!, $publish: Boolean!, $hashtags: [HashtagInput!], $impersonatedAs: ID) {
              createKnowledgeCard(
                data: {knowledgeCardInfo: {detail: {type: DATA_DOCUMENT, dataDocument: {title: $name, content: $content}}, hashtags: $hashtags}, isPublished: $publish, impersonatedAs: $impersonatedAs}
              ) {
                id
              }
            }
            """
        )
        variables: Dict[str, object] = {
            "name": name,
            "content": content,
            "publish": publish,
            "hashtags": hashtags,
            "impersonatedAs": impersonated_as,
        }
        response = self.execute(
            query=query,
            operation_name="createDataDocument",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return CreateDataDocument.model_validate(data)

    def create_namespace(
        self,
        name: str,
        parent_id: Union[Optional[str], UnsetType] = UNSET,
        **kwargs: Any
    ) -> CreateNamespace:
        query = gql(
            """
            mutation createNamespace($name: String!, $parentId: ID) {
              createNamespace(
                data: {namespaceInfo: {name: $name, detail: {type: USER_DEFINED_SPACE}, parentId: $parentId}}
              ) {
                id
              }
            }
            """
        )
        variables: Dict[str, object] = {"name": name, "parentId": parent_id}
        response = self.execute(
            query=query, operation_name="createNamespace", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return CreateNamespace.model_validate(data)

    def delete_data_document(self, id: str, **kwargs: Any) -> DeleteDataDocument:
        query = gql(
            """
            mutation deleteDataDocument($id: ID!) {
              deleteKnowledgeCards(input: {ids: [$id]}) {
                deletedIds
                failedIds
              }
            }
            """
        )
        variables: Dict[str, object] = {"id": id}
        response = self.execute(
            query=query,
            operation_name="deleteDataDocument",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return DeleteDataDocument.model_validate(data)

    def update_custom_metadata_config(
        self, input: UpdateCustomMetadataConfigInput, **kwargs: Any
    ) -> UpdateCustomMetadataConfig:
        query = gql(
            """
            mutation updateCustomMetadataConfig($input: UpdateCustomMetadataConfigInput!) {
              updateCustomMetadataConfig(input: $input) {
                key
                displayName
                dataType
                searchable
                highlight
                searchable
              }
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = self.execute(
            query=query,
            operation_name="updateCustomMetadataConfig",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return UpdateCustomMetadataConfig.model_validate(data)

    def create_domain(
        self,
        name: str,
        description: Union[Optional[NamespaceDescriptionInput], UnsetType] = UNSET,
        color: Union[Optional[str], UnsetType] = UNSET,
        icon_key: Union[Optional[str], UnsetType] = UNSET,
        parent_id: Union[Optional[str], UnsetType] = UNSET,
        **kwargs: Any
    ) -> CreateDomain:
        query = gql(
            """
            mutation createDomain($name: String!, $description: NamespaceDescriptionInput, $color: String, $iconKey: String, $parentId: ID) {
              createNamespace(
                data: {namespaceInfo: {name: $name, description: $description, detail: {type: DATA_GROUP}, customAttributes: {color: $color, iconKey: $iconKey}, parentId: $parentId}}
              ) {
                id
              }
            }
            """
        )
        variables: Dict[str, object] = {
            "name": name,
            "description": description,
            "color": color,
            "iconKey": icon_key,
            "parentId": parent_id,
        }
        response = self.execute(
            query=query, operation_name="createDomain", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return CreateDomain.model_validate(data)

    def delete_domain(self, id: str, **kwargs: Any) -> DeleteDomain:
        query = gql(
            """
            mutation deleteDomain($id: ID!) {
              deleteNamespaces(input: {ids: [$id]}) {
                deletedIds
                failedIds
              }
            }
            """
        )
        variables: Dict[str, object] = {"id": id}
        response = self.execute(
            query=query, operation_name="deleteDomain", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return DeleteDomain.model_validate(data)

    def update_domain_assets(
        self,
        id: str,
        asset_ids_to_add: Union[Optional[List[str]], UnsetType] = UNSET,
        asset_ids_to_remove: Union[Optional[List[str]], UnsetType] = UNSET,
        collection_name: Union[Optional[str], UnsetType] = UNSET,
        remove_collection: Union[Optional[bool], UnsetType] = UNSET,
        **kwargs: Any
    ) -> UpdateDomainAssets:
        query = gql(
            """
            mutation updateDomainAssets($id: ID!, $assetIdsToAdd: [ID!], $assetIdsToRemove: [ID!], $collectionName: String, $removeCollection: Boolean = false) {
              updateNamespaceAssets(
                input: {entityIds: [$id], assetIdsToAdd: $assetIdsToAdd, assetIdsToRemove: $assetIdsToRemove, namedAssetCollectionName: $collectionName, removeCollection: $removeCollection}
              ) {
                id
              }
            }
            """
        )
        variables: Dict[str, object] = {
            "id": id,
            "assetIdsToAdd": asset_ids_to_add,
            "assetIdsToRemove": asset_ids_to_remove,
            "collectionName": collection_name,
            "removeCollection": remove_collection,
        }
        response = self.execute(
            query=query,
            operation_name="updateDomainAssets",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return UpdateDomainAssets.model_validate(data)

    def update_domain_info(
        self,
        id: str,
        parent_id: Union[Optional[str], UnsetType] = UNSET,
        name: Union[Optional[str], UnsetType] = UNSET,
        description: Union[Optional[NamespaceDescriptionInput], UnsetType] = UNSET,
        color: Union[Optional[str], UnsetType] = UNSET,
        icon_key: Union[Optional[str], UnsetType] = UNSET,
        **kwargs: Any
    ) -> UpdateDomainInfo:
        query = gql(
            """
            mutation updateDomainInfo($id: ID!, $parentId: ID, $name: String, $description: NamespaceDescriptionInput, $color: String, $iconKey: String) {
              patchUpdateNamespaceInfo(
                input: {entityId: $id, parentId: $parentId, name: $name, description: $description, customAttributes: {color: $color, iconKey: $iconKey}}
              ) {
                id
              }
            }
            """
        )
        variables: Dict[str, object] = {
            "id": id,
            "parentId": parent_id,
            "name": name,
            "description": description,
            "color": color,
            "iconKey": icon_key,
        }
        response = self.execute(
            query=query,
            operation_name="updateDomainInfo",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return UpdateDomainInfo.model_validate(data)

    def update_domain_saved_queries(
        self,
        id: str,
        saved_queries: List[SavedLiveQueryInput],
        name: Union[Optional[str], UnsetType] = UNSET,
        description: Union[Optional[NamespaceDescriptionInput], UnsetType] = UNSET,
        visible_to: Union[Optional[List[str]], UnsetType] = UNSET,
        custom_attributes: Union[Optional[CustomAttributesInput], UnsetType] = UNSET,
        parent_id: Union[Optional[str], UnsetType] = UNSET,
        **kwargs: Any
    ) -> UpdateDomainSavedQueries:
        query = gql(
            """
            mutation updateDomainSavedQueries($id: ID!, $savedQueries: [SavedLiveQueryInput!]!, $name: String, $description: NamespaceDescriptionInput, $visibleTo: [ID!], $customAttributes: CustomAttributesInput, $parentId: ID) {
              updateNamespaceInfo(
                data: {entityId: $id, detail: {savedQueries: $savedQueries, type: DATA_GROUP}, name: $name, description: $description, visibleTo: $visibleTo, customAttributes: $customAttributes, parentId: $parentId}
              ) {
                id
              }
            }
            """
        )
        variables: Dict[str, object] = {
            "id": id,
            "savedQueries": saved_queries,
            "name": name,
            "description": description,
            "visibleTo": visible_to,
            "customAttributes": custom_attributes,
            "parentId": parent_id,
        }
        response = self.execute(
            query=query,
            operation_name="updateDomainSavedQueries",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return UpdateDomainSavedQueries.model_validate(data)

    def add_governed_tags(
        self, input: List[UserDefinedResourceInput], **kwargs: Any
    ) -> AddGovernedTags:
        query = gql(
            """
            mutation addGovernedTags($input: [UserDefinedResourceInput!]!) {
              createUserDefinedResource(input: $input) {
                id
              }
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = self.execute(
            query=query, operation_name="addGovernedTags", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return AddGovernedTags.model_validate(data)

    def assign_governed_tags(
        self, input: List[AssetGovernedTagsPatchInput], **kwargs: Any
    ) -> AssignGovernedTags:
        query = gql(
            """
            mutation assignGovernedTags($input: [AssetGovernedTagsPatchInput!]!) {
              upsertAssetGovernedTags(input: $input) {
                __typename
                id
              }
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = self.execute(
            query=query,
            operation_name="assignGovernedTags",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return AssignGovernedTags.model_validate(data)

    def remove_governed_tags(
        self, input: UserDefinedResourceDeleteInput, **kwargs: Any
    ) -> RemoveGovernedTags:
        query = gql(
            """
            mutation removeGovernedTags($input: UserDefinedResourceDeleteInput!) {
              deleteUserDefinedResource(input: $input) {
                deletedIds
                failedIds
              }
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = self.execute(
            query=query,
            operation_name="removeGovernedTags",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return RemoveGovernedTags.model_validate(data)

    def unassign_governed_tags(
        self, input: List[AssetGovernedTagsPatchInput], **kwargs: Any
    ) -> UnassignGovernedTags:
        query = gql(
            """
            mutation unassignGovernedTags($input: [AssetGovernedTagsPatchInput!]!) {
              upsertAssetGovernedTags(input: $input) {
                __typename
                id
              }
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = self.execute(
            query=query,
            operation_name="unassignGovernedTags",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return UnassignGovernedTags.model_validate(data)

    def update_settings(self, input: SettingsInput, **kwargs: Any) -> UpdateSettings:
        query = gql(
            """
            mutation updateSettings($input: SettingsInput!) {
              updateSettings(input: $input) {
                __typename
              }
            }
            """
        )
        variables: Dict[str, object] = {"input": input}
        response = self.execute(
            query=query, operation_name="updateSettings", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return UpdateSettings.model_validate(data)

    def add_webhook(
        self, trigger: WebhookTriggerType, url: str, **kwargs: Any
    ) -> AddWebhook:
        query = gql(
            """
            mutation addWebhook($trigger: WebhookTriggerType!, $url: String!) {
              addWebhook(input: {trigger: $trigger, url: $url}) {
                _id
              }
            }
            """
        )
        variables: Dict[str, object] = {"trigger": trigger, "url": url}
        response = self.execute(
            query=query, operation_name="addWebhook", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return AddWebhook.model_validate(data)

    def remove_webhook(self, id: str, **kwargs: Any) -> RemoveWebhook:
        query = gql(
            """
            mutation removeWebhook($id: ID!) {
              deleteWebhooks(input: {ids: [$id]}) {
                deletedIds
              }
            }
            """
        )
        variables: Dict[str, object] = {"id": id}
        response = self.execute(
            query=query, operation_name="removeWebhook", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return RemoveWebhook.model_validate(data)

    def get_domain_assets(
        self,
        id: str,
        end_cursor: Union[Optional[str], UnsetType] = UNSET,
        **kwargs: Any
    ) -> GetDomainAssets:
        query = gql(
            """
            query getDomainAssets($id: ID!, $endCursor: String) {
              node(id: $id) {
                __typename
                ... on Namespace {
                  namespaceAssets {
                    assets(first: 50, after: $endCursor) {
                      edges {
                        node {
                          __typename
                          id
                        }
                      }
                      pageInfo {
                        hasNextPage
                        endCursor
                      }
                    }
                  }
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"id": id, "endCursor": end_cursor}
        response = self.execute(
            query=query, operation_name="getDomainAssets", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return GetDomainAssets.model_validate(data)

    def get_custom_metadata_settings(self, **kwargs: Any) -> GetCustomMetadataSettings:
        query = gql(
            """
            query getCustomMetadataSettings {
              settings {
                customMetadataConfig {
                  key
                  displayName
                  dataType
                  highlight
                  searchable
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {}
        response = self.execute(
            query=query,
            operation_name="getCustomMetadataSettings",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return GetCustomMetadataSettings.model_validate(data)

    def get_data_document(self, id: str, **kwargs: Any) -> GetDataDocument:
        query = gql(
            """
            query getDataDocument($id: ID!) {
              node(id: $id) {
                __typename
                ... on KnowledgeCard {
                  knowledgeCardInfo {
                    created {
                      time
                      actor
                    }
                    lastModified {
                      time
                      actor
                    }
                    detail {
                      type
                      dataDocument {
                        title
                        content
                        tokenizedContent {
                          content
                        }
                      }
                    }
                  }
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"id": id}
        response = self.execute(
            query=query, operation_name="getDataDocument", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return GetDataDocument.model_validate(data)

    def get_dataset_governed_tags(
        self,
        id: str,
        end_cursor: Union[Optional[str], UnsetType] = UNSET,
        **kwargs: Any
    ) -> GetDatasetGovernedTags:
        query = gql(
            """
            query getDatasetGovernedTags($id: ID!, $endCursor: String) {
              node(id: $id) {
                __typename
                ... on Dataset {
                  governedTags(first: 50, after: $endCursor) {
                    edges {
                      node {
                        id
                        userDefinedResourceInfo {
                          name
                          description {
                            text
                          }
                        }
                      }
                    }
                    pageInfo {
                      endCursor
                      hasNextPage
                    }
                  }
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"id": id, "endCursor": end_cursor}
        response = self.execute(
            query=query,
            operation_name="getDatasetGovernedTags",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return GetDatasetGovernedTags.model_validate(data)

    def get_namespaces(
        self,
        type: NamespaceType,
        name: Union[Optional[str], UnsetType] = UNSET,
        parent_id: Union[Optional[List[str]], UnsetType] = UNSET,
        end_cursor: Union[Optional[str], UnsetType] = UNSET,
        **kwargs: Any
    ) -> GetNamespaces:
        query = gql(
            """
            query getNamespaces($name: String, $parentId: [ID!], $endCursor: String, $type: NamespaceType!) {
              namespaces(
                first: 20
                filters: {name: $name, type: [$type], isChildOf: $parentId}
                after: $endCursor
              ) {
                edges {
                  node {
                    id
                    ...NamespaceParts
                  }
                }
                pageInfo {
                  hasNextPage
                  endCursor
                }
              }
            }

            fragment NamespaceParts on Namespace {
              namespaceInfo {
                name
                created {
                  time
                  actor
                }
                lastModified {
                  time
                  actor
                }
                detail {
                  savedQueries {
                    name
                    keyword
                    context
                    id
                    facetsJSON
                  }
                }
                visibleTo
                description {
                  text
                  tokenizedText
                }
                customAttributes {
                  color
                  iconKey
                }
              }
              parentNamespace {
                id
              }
              namespaceAssets {
                namedAssetCollections {
                  name
                  assetIds
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {
            "name": name,
            "parentId": parent_id,
            "endCursor": end_cursor,
            "type": type,
        }
        response = self.execute(
            query=query, operation_name="getNamespaces", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return GetNamespaces.model_validate(data)

    def get_domain(self, id: str, **kwargs: Any) -> GetDomain:
        query = gql(
            """
            query getDomain($id: ID!) {
              node(id: $id) {
                __typename
                ...NamespaceParts
              }
            }

            fragment NamespaceParts on Namespace {
              namespaceInfo {
                name
                created {
                  time
                  actor
                }
                lastModified {
                  time
                  actor
                }
                detail {
                  savedQueries {
                    name
                    keyword
                    context
                    id
                    facetsJSON
                  }
                }
                visibleTo
                description {
                  text
                  tokenizedText
                }
                customAttributes {
                  color
                  iconKey
                }
              }
              parentNamespace {
                id
              }
              namespaceAssets {
                namedAssetCollections {
                  name
                  assetIds
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"id": id}
        response = self.execute(
            query=query, operation_name="getDomain", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return GetDomain.model_validate(data)

    def get_non_prod_settings(self, **kwargs: Any) -> GetNonProdSettings:
        query = gql(
            """
            query getNonProdSettings {
              settings {
                nonProd {
                  datasetPatterns {
                    platform
                    account
                    database
                    schema
                    table
                    isCaseSensitive
                  }
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {}
        response = self.execute(
            query=query,
            operation_name="getNonProdSettings",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return GetNonProdSettings.model_validate(data)

    def get_setup_info(self, **kwargs: Any) -> GetSetupInfo:
        query = gql(
            """
            query getSetupInfo {
              setupInfo {
                oidc {
                  signInRedirectUrl
                }
                saml {
                  entityId
                  replyACSUrl
                  signOnUrl
                }
                crawlerIpAddresses
              }
            }
            """
        )
        variables: Dict[str, object] = {}
        response = self.execute(
            query=query, operation_name="getSetupInfo", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return GetSetupInfo.model_validate(data)

    def get_soft_deletion_settings(self, **kwargs: Any) -> GetSoftDeletionSettings:
        query = gql(
            """
            query getSoftDeletionSettings {
              settings {
                softDeletion {
                  enabled
                  thresholdHours
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {}
        response = self.execute(
            query=query,
            operation_name="getSoftDeletionSettings",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return GetSoftDeletionSettings.model_validate(data)

    def get_user(self, email: str, **kwargs: Any) -> GetUser:
        query = gql(
            """
            query getUser($email: String!) {
              person(logicalId: {email: $email}) {
                id
              }
            }
            """
        )
        variables: Dict[str, object] = {"email": email}
        response = self.execute(
            query=query, operation_name="getUser", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return GetUser.model_validate(data)

    def get_webhook_payload_schema(
        self, trigger: WebhookTriggerType, **kwargs: Any
    ) -> GetWebhookPayloadSchema:
        query = gql(
            """
            query getWebhookPayloadSchema($trigger: WebhookTriggerType!) {
              webhookPayloadSchema(input: {trigger: $trigger})
            }
            """
        )
        variables: Dict[str, object] = {"trigger": trigger}
        response = self.execute(
            query=query,
            operation_name="getWebhookPayloadSchema",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return GetWebhookPayloadSchema.model_validate(data)

    def get_webhooks(
        self,
        trigger: Union[Optional[WebhookTriggerType], UnsetType] = UNSET,
        **kwargs: Any
    ) -> GetWebhooks:
        query = gql(
            """
            query getWebhooks($trigger: WebhookTriggerType) {
              webhooks(input: {trigger: $trigger}) {
                _id
              }
            }
            """
        )
        variables: Dict[str, object] = {"trigger": trigger}
        response = self.execute(
            query=query, operation_name="getWebhooks", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return GetWebhooks.model_validate(data)

    def get_governed_tag(self, id: str, **kwargs: Any) -> GetGovernedTag:
        query = gql(
            """
            query getGovernedTag($id: ID!) {
              node(id: $id) {
                __typename
                ... on UserDefinedResource {
                  id
                  userDefinedResourceInfo {
                    name
                    description {
                      text
                    }
                  }
                  parentResource {
                    id
                    userDefinedResourceInfo {
                      name
                    }
                  }
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"id": id}
        response = self.execute(
            query=query, operation_name="getGovernedTag", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return GetGovernedTag.model_validate(data)

    def get_governed_tag_child_tags(
        self,
        id: str,
        end_cursor: Union[Optional[str], UnsetType] = UNSET,
        **kwargs: Any
    ) -> GetGovernedTagChildTags:
        query = gql(
            """
            query getGovernedTagChildTags($id: ID!, $endCursor: String) {
              node(id: $id) {
                __typename
                ... on UserDefinedResource {
                  childResources(first: 50, after: $endCursor, filters: {type: [GOVERNED_TAG]}) {
                    edges {
                      node {
                        id
                        userDefinedResourceInfo {
                          name
                          description {
                            text
                          }
                        }
                        parentResource {
                          id
                          userDefinedResourceInfo {
                            name
                          }
                        }
                      }
                    }
                    pageInfo {
                      hasNextPage
                      endCursor
                    }
                  }
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"id": id, "endCursor": end_cursor}
        response = self.execute(
            query=query,
            operation_name="getGovernedTagChildTags",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return GetGovernedTagChildTags.model_validate(data)

    def list_governed_tags(
        self,
        name: Union[Optional[str], UnsetType] = UNSET,
        end_cursor: Union[Optional[str], UnsetType] = UNSET,
        **kwargs: Any
    ) -> ListGovernedTags:
        query = gql(
            """
            query listGovernedTags($name: String, $endCursor: String) {
              userDefinedResources(
                first: 50
                after: $endCursor
                filters: {name: $name, type: [GOVERNED_TAG]}
              ) {
                edges {
                  node {
                    id
                    userDefinedResourceInfo {
                      name
                      description {
                        text
                      }
                    }
                    parentResource {
                      id
                      userDefinedResourceInfo {
                        name
                      }
                    }
                  }
                }
                pageInfo {
                  hasNextPage
                  endCursor
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"name": name, "endCursor": end_cursor}
        response = self.execute(
            query=query,
            operation_name="listGovernedTags",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return ListGovernedTags.model_validate(data)
