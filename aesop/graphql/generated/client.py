# Generated by ariadne-codegen
# Source: aesop/graphql/queries

from typing import Any, Dict, List, Optional, Union

from .add_governed_tags import AddGovernedTags
from .assign_governed_tags import AssignGovernedTags
from .base_client import BaseClient
from .base_model import UNSET, UnsetType
from .create_knowledge_card import CreateKnowledgeCard
from .get_custom_metadata_settings import GetCustomMetadataSettings
from .get_dataset_governed_tags import GetDatasetGovernedTags
from .get_governed_tags import GetGovernedTags
from .get_non_prod_settings import GetNonProdSettings
from .get_setup_info import GetSetupInfo
from .get_soft_deletion_settings import GetSoftDeletionSettings
from .input_types import (
    AssetGovernedTagsPatchInput,
    KnowledgeCardInput,
    SettingsInput,
    UserDefinedResourceDeleteInput,
    UserDefinedResourceInput,
)
from .remove_governed_tags import RemoveGovernedTags
from .unassign_governed_tags import UnassignGovernedTags
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

    def get_governed_tags(
        self,
        name: Union[Optional[str], UnsetType] = UNSET,
        end_cursor: Union[Optional[str], UnsetType] = UNSET,
        **kwargs: Any
    ) -> GetGovernedTags:
        query = gql(
            """
            query getGovernedTags($name: String, $endCursor: String) {
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
            query=query, operation_name="getGovernedTags", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return GetGovernedTags.model_validate(data)

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
