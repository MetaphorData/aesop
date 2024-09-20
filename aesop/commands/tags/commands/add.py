from typing import Optional

from aesop.commands.common.exception_handler import exception_handler
from aesop.config import AesopConfig
from aesop.console import console
from aesop.graphql.generated.enums import UserDefinedResourceType
from aesop.graphql.generated.input_types import (
    UserDefinedResourceDescriptionInput,
    UserDefinedResourceInfoInput,
    UserDefinedResourceInput,
)


@exception_handler("add tag", exception_type=Exception)
def add(
    name: str,
    description: Optional[str],
    config: AesopConfig,
) -> None:
    client = config.get_graphql_client()
    id = (
        client.create_governed_tag(
            input=[
                UserDefinedResourceInput(
                    userDefinedResourceInfo=UserDefinedResourceInfoInput(
                        name=name,
                        type=UserDefinedResourceType.GOVERNED_TAG,
                        description=(
                            UserDefinedResourceDescriptionInput(text=description)
                            if description
                            else None
                        ),
                    )
                )
            ]
        )
        .create_user_defined_resource[0]
        .id
    )
    console.ok(f"Created governed tag, id = {id}")
