import json
from tempfile import NamedTemporaryFile
from typing import List

from pydantic import TypeAdapter

from aesop.commands.aspects.custom_metadata import _Item
from tests.base_test_suite import BaseTestSuite


class TestCustomMetadata(BaseTestSuite):
    def test_add_get_then_remove_custom_metadata(self) -> None:
        # Create bogus name and description
        items = {
            self.gen_rand_str(10): "0.12345",
            self.gen_rand_str(10): '"this is a string"',
            self.gen_rand_str(10): '{"name": "john doe"}',
        }
        entity_id = "DATASET~8CDF81FE6B8050607E78C53E8B704B05"
        with NamedTemporaryFile("w+") as f:
            f.write(
                json.dumps(
                    {
                        "entity_id": entity_id,
                        "set": [
                            {"key": key, "value": value} for key, value in items.items()
                        ],
                    }
                )
            )
            f.seek(0)
            res = self.run_app(
                [
                    "custom-metadata",
                    "update",
                    f.name,
                ]
            )
            assert res.exit_code == 0

        res = self.run_app(
            [
                "custom-metadata",
                "get",
                entity_id,
            ]
        )
        assert res.exit_code == 0
        metadata = {
            item.key: item.value
            for item in TypeAdapter(List[_Item]).validate_json(res.stdout)
        }
        for key, value in items.items():
            assert key in metadata
            assert metadata[key] == value

        with NamedTemporaryFile("w+") as f:
            f.write(
                json.dumps(
                    {
                        "entity_id": entity_id,
                        "unset": list(items.keys()),
                    }
                )
            )
            f.seek(0)
            res = self.run_app(
                [
                    "custom-metadata",
                    "update",
                    f.name,
                ]
            )
            assert res.exit_code == 0

        res = self.run_app(
            [
                "custom-metadata",
                "get",
                entity_id,
            ]
        )
        assert res.exit_code == 0
        metadata = {
            item.key: item.value
            for item in TypeAdapter(List[_Item]).validate_json(res.stdout)
        }
        for key, value in items.items():
            assert key not in metadata
