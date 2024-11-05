import json

from aesop.commands.aspects.user_defined_resources.tags.models import (
    AddTagsOutput,
    RemoveTagsOutput,
)
from aesop.commands.aspects.user_defined_resources.tags.node import GovernedTagNode
from tests.base_test_suite import BaseTestSuite
from tests.utils import gen_random_str


class TestTags(BaseTestSuite):

    def test_add_get_then_remove_tag(self) -> None:

        # Create bogus name and description
        name = gen_random_str(10)
        description = gen_random_str(40)

        # Add a tag
        res = self.run_app(
            [
                "tags",
                "add",
                name,
                "--description",
                description,
            ]
        )
        assert res.exit_code == 0
        added_tags = AddTagsOutput.model_validate_json(res.stdout)
        assert len(added_tags.created_ids) == 1
        created_tag_id = added_tags.created_ids[0]

        # See if the tag exists
        res = self.run_app(
            [
                "tags",
                "list",
                "--name",
                name,
            ]
        )
        assert res.exit_code == 0

        tags = json.loads(res.stdout)
        assert isinstance(tags, list) and tags
        node = GovernedTagNode.model_validate(tags[0])
        assert node.name == name
        assert node.description == description
        assert node.id == created_tag_id

        # Remove the tag
        res = self.run_app(
            [
                "tags",
                "remove",
                created_tag_id,
            ]
        )
        assert res.exit_code == 0
        removed_tags = RemoveTagsOutput.model_validate_json(
            res.stdout.replace("\n", "")
        )
        assert not removed_tags.failed_ids
        assert removed_tags.removed_ids == [created_tag_id]

        # See if the tag no longer exists
        res = self.run_app(
            [
                "tags",
                "list",
                "--name",
                name,
            ]
        )
        assert res.exit_code == 0

        tags = json.loads(res.stdout)
        assert isinstance(tags, list) and not tags
