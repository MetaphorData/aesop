from aesop.commands.tags.models import AddTagsInput
from aesop.config import AesopConfig
from aesop.console import console
from aesop.graphql.generated.enums import UserDefinedResourceType
from aesop.graphql.generated.input_types import (
    UserDefinedResourceDescriptionInput,
    UserDefinedResourceInfoInput,
    UserDefinedResourceInput,
)


def add(
    add_tags_input: AddTagsInput,
    config: AesopConfig,
) -> None:
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
        for tag in add_tags_input.tags
    ]
    resp = client.add_governed_tags(input=input)
    if not resp.create_user_defined_resource:
        raise ValueError
    created_ids = [res.id for res in resp.create_user_defined_resource]
    console.ok("Successfully created governed tags")
    console.print(created_ids)
