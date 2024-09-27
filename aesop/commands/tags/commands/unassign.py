from aesop.commands.tags.models import AssignTagsInput
from aesop.config import AesopConfig
from aesop.console import console
from aesop.graphql.generated.input_types import AssetGovernedTagsPatchInput


def unassign(
    input: AssignTagsInput,
    config: AesopConfig,
) -> None:
    client = config.get_graphql_client()
    ids = [
        res.id
        for res in client.unassign_governed_tags(
            input=[
                AssetGovernedTagsPatchInput(
                    entityIds=input.asset_ids,
                    governedTagsToRemove=input.tag_ids,
                ),
            ]
        ).upsert_asset_governed_tags
    ]
    console.ok(f"Unassigned governed tags {input.tag_ids} from assets {ids}")
