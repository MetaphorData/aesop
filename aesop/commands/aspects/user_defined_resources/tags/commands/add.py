from typing import List

from aesop.commands.aspects.user_defined_resources.tags.models import GovernedTag
from aesop.config import AesopConfig
from aesop.graphql.generated.enums import UserDefinedResourceType
from aesop.graphql.generated.input_types import (
    UserDefinedResourceDescriptionInput,
    UserDefinedResourceInfoInput,
    UserDefinedResourceInput,
)


def add_tags(
    tags: List[GovernedTag],
    config: AesopConfig,
) -> List[str]:
    client = config.get_graphql_client()
    input = [
        UserDefinedResourceInput(
            userDefinedResourceInfo=UserDefinedResourceInfoInput(
                name=tag.name,
                type=UserDefinedResourceType.GOVERNED_TAG,
                description=(
                    UserDefinedResourceDescriptionInput(text=tag.description)
                    if tag.description
                    else None
                ),
            )
        )
        for tag in tags
    ]
    resp = client.add_governed_tags(input=input)
    if not resp.create_user_defined_resource:
        raise ValueError
    created_ids = [res.id for res in resp.create_user_defined_resource]
    return created_ids
