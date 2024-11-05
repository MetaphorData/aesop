import json
from typing import List

from pydantic import TypeAdapter

from aesop.graphql.generated.get_domain import GetDomainNodeNamespace
from tests.base_test_suite import BaseTestSuite
from tests.utils import gen_random_str


class TestDomains(BaseTestSuite):
    def test_add_then_remove_domain(self) -> None:
        def create_parent() -> tuple[str, str]:
            parent_name = gen_random_str(10)
            resp = self.run_app(
                ["domains", "add", parent_name, "--description", "parent"]
            )
            assert not resp.exit_code
            assert resp.output.startswith("Created domain:")
            parent_id = resp.output[len("Created domain: ") : -1]
            return parent_name, parent_id

        def create_child(parent_id: str) -> tuple[str, str]:
            child_name = gen_random_str(10)
            resp = self.run_app(
                [
                    "domains",
                    "add",
                    child_name,
                    "--description",
                    "child",
                    "--parent-id",
                    parent_id,
                ]
            )
            assert not resp.exit_code
            assert resp.output.startswith("Created domain:")
            child_id = resp.output[len("Created domain: ") : -1]
            return child_name, child_id

        def list_domains(child_id: str, parent_id: str) -> None:
            resp = self.run_app(["domains", "list"])
            assert not resp.exit_code
            domains = json.loads(resp.output)
            assert next((d for d in domains if d["id"] == parent_id), None)
            assert next((d for d in domains if d["id"] == child_id), None)

        def get_parent(
            parent_id: str, parent_name: str, should_exist: bool = True
        ) -> None:
            parent_resp = self.run_app(["domains", "get", parent_id])
            assert not parent_resp.exit_code
            if not should_exist:
                assert not parent_resp.output
                return

            parent_domain = GetDomainNodeNamespace.model_validate_json(
                parent_resp.output
            )
            assert (
                parent_domain.namespace_info
                and parent_domain.namespace_info.name == parent_name
            )

        def get_child(
            child_id: str, child_name: str, parent_id: str, should_exist: bool = True
        ) -> None:
            child_resp = self.run_app(["domains", "get", child_id])
            assert not child_resp.exit_code
            if not should_exist:
                assert not child_resp.output
                return
            child_domain = GetDomainNodeNamespace.model_validate_json(child_resp.output)
            assert (
                child_domain.namespace_info
                and child_domain.namespace_info.name == child_name
            )
            assert (
                child_domain.parent_namespace
                and child_domain.parent_namespace.id == parent_id
            )

        def delete_parent(parent_id: str, child_id: str) -> None:
            resp = self.run_app(["domains", "remove", parent_id])
            assert not resp.exit_code
            assert resp.stdout.startswith("Deleted domains: ")
            assert not resp.stderr
            deleted = TypeAdapter(List[str]).validate_json(
                resp.stdout[len("Deleted domains: ") : -1]
                .replace("\n", "")
                .replace("'", '"')
            )
            assert parent_id in deleted
            assert child_id in deleted

        # Create parent and child domains
        parent_name, parent_id = create_parent()
        child_name, child_id = create_child(parent_id)

        # Confirm both exist
        get_parent(parent_id, parent_name)
        get_child(child_id, child_name, parent_id)
        list_domains(child_id, parent_id)

        # Just delete parent here, Metaphor will delete children for us
        delete_parent(parent_id, child_id)

        # Check neither parent nor child can be found
        get_parent(parent_id, parent_name, should_exist=False)
        get_child(child_id, child_name, parent_id, should_exist=False)
