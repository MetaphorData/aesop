from aesop.commands.tags.models import AssignTagsInput
from aesop.config import AesopConfig
from aesop.console import console
from aesop.graphql.generated.input_types import AssetGovernedTagsPatchInput


def assign(
    input: AssignTagsInput,
    config: AesopConfig,
) -> None:
    client = config.get_graphql_client()
    ids = [
        res.id
        for res in client.assign_governed_tags(
            input=[
                AssetGovernedTagsPatchInput(
                    entityIds=input.asset_ids,
                    governedTagsToAdd=input.tag_ids,
                ),
            ]
        ).upsert_asset_governed_tags
    ]
    console.ok(f"Assigned governed tags {input.tag_ids} to assets {ids}")
