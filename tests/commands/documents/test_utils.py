from aesop.commands.documents.utils import get_user_id
from tests.base_test_suite import BaseTestSuite


class TestDocumentUtils(BaseTestSuite):
    def test_get_user_id(self) -> None:
        # E2E user, always exists
        user_id = "PERSON~2EC0695837F8ED0B0358C0250B2BCE34"
        email = "test-only@metaphor.io"
        assert get_user_id(self.graphql_client, user_id) == user_id
        assert get_user_id(self.graphql_client, email) == user_id
