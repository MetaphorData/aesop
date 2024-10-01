from typing import List, Optional

from aesop.commands.tags.models import BatchAddTagsInput, GovernedTag
from aesop.config import AesopConfig
from aesop.console import console
from aesop.graphql.generated.enums import UserDefinedResourceType
from aesop.graphql.generated.input_types import (
    UserDefinedResourceDescriptionInput,
    UserDefinedResourceInfoInput,
    UserDefinedResourceInput,
)


def _add_tags(
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


def add(
    name: str,
    description: Optional[str],
    config: AesopConfig,
) -> None:
    tag = GovernedTag(name=name, description=description)
    created_ids = _add_tags([tag], config)
    console.ok("Successfully created governed tag")
    console.print(created_ids[0])


def batch_add(
    batch_add_tags_input: BatchAddTagsInput,
    config: AesopConfig,
) -> None:
    created_ids = _add_tags(batch_add_tags_input.tags, config)
    console.ok("Successfully created governed tags")
    console.print(created_ids)
