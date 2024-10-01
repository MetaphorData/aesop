from typing import List

from aesop.config import AesopConfig
from aesop.graphql.generated.input_types import AssetGovernedTagsPatchInput


def unassign_tags(
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
