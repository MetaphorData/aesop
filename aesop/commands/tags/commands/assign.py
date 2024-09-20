from aesop.config import AesopConfig
from aesop.console import console
from aesop.graphql.generated.input_types import AssetGovernedTagsPatchInput


def assign(
    entity_id: str,
    tag_id: str,
    config: AesopConfig,
):
    client = config.get_graphql_client()
    id = (
        client.assign_governed_tag(
            input=[
                AssetGovernedTagsPatchInput(
                    entityIds=[entity_id],
                    governedTagsToAdd=[tag_id],
                ),
            ]
        )
        .upsert_asset_governed_tags[0]
        .id
    )
    console.ok(f"Assigned tag to {id}")
