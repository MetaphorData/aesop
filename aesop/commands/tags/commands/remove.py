from rich import print

from aesop.commands.tags.models import RemoveTagsInput
from aesop.config import AesopConfig
from aesop.graphql.generated.input_types import UserDefinedResourceDeleteInput


def remove(
    input: RemoveTagsInput,
    config: AesopConfig,
) -> None:
    client = config.get_graphql_client()
    resp = client.remove_governed_tags(
        input=UserDefinedResourceDeleteInput(
            ids=input.tag_ids,
        )
    ).delete_user_defined_resource
    print(resp.model_dump_json(indent=2))
