from typing import List

from aesop.config import AesopConfig
from aesop.graphql.generated.input_types import UserDefinedResourceDeleteInput
from aesop.graphql.generated.remove_governed_tags import RemoveGovernedTags


def remove_tags(
    tag_ids: List[str],
    config: AesopConfig,
) -> RemoveGovernedTags:
    client = config.get_graphql_client()
    return client.remove_governed_tags(
        input=UserDefinedResourceDeleteInput(
            ids=tag_ids,
        )
    )
