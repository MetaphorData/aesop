from typing import List

from rich import print

from aesop.commands.tags.models import BatchRemoveTagsInput
from aesop.config import AesopConfig
from aesop.graphql.generated.input_types import UserDefinedResourceDeleteInput
from aesop.graphql.generated.remove_governed_tags import RemoveGovernedTags


def _remove_tags(
    tag_ids: List[str],
    config: AesopConfig,
) -> RemoveGovernedTags:
    client = config.get_graphql_client()
    return client.remove_governed_tags(
        input=UserDefinedResourceDeleteInput(
            ids=tag_ids,
        )
    )


def remove(
    tag_id: str,
    config: AesopConfig,
) -> None:
    _remove_tags([tag_id], config)
    print(f"Removed tag {tag_id}")


def batch_remove(
    input: BatchRemoveTagsInput,
    config: AesopConfig,
) -> None:
    resp = _remove_tags(input.tag_ids, config)
    print(resp.model_dump_json(indent=2))
