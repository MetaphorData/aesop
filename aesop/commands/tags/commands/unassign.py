from typing import List

from aesop.commands.tags.models import BatchAssignTagsInput
from aesop.config import AesopConfig
from aesop.console import console
from aesop.graphql.generated.input_types import AssetGovernedTagsPatchInput


def _unassign_tags(
    tag_ids: List[str],
    asset_ids: List[str],
    config: AesopConfig,
) -> List[str]:
    client = config.get_graphql_client()
    return [
        res.id
        for res in client.unassign_governed_tags(
            input=[
                AssetGovernedTagsPatchInput(
                    entityIds=asset_ids,
                    governedTagsToRemove=tag_ids,
                ),
            ]
        ).upsert_asset_governed_tags
    ]


def unassign(
    tag_id: str,
    asset_id: str,
    config: AesopConfig,
) -> None:
    ids = _unassign_tags([tag_id], [asset_id], config)
    console.ok(f"Unassigned governed tag {tag_id} from asset {ids[0]}")


def batch_unassign(
    input: BatchAssignTagsInput,
    config: AesopConfig,
) -> None:
    ids = _unassign_tags(input.tag_ids, input.asset_ids, config)
    console.ok(f"Unassigned governed tags {input.tag_ids} from assets {ids}")
