import random
import string

from aesop.graphql.generated.enums import DataPlatform
from aesop.graphql.generated.get_non_prod_settings import (
    GetNonProdSettingsSettingsNonProd,
)
from aesop.graphql.generated.input_types import DatasetPatternInput
from tests.base_test_suite import BaseTestSuite


class TestNonProd(BaseTestSuite):

    def test_add_then_remove_non_prod(self) -> None:
        name = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
        database = '"*"'
        schema = '"*"'
        table = name
        platform = DataPlatform.BIGQUERY
        target_pattern = DatasetPatternInput(
            account=None,
            database=database,
            isCaseSensitive=False,
            platform=platform,
            schema=schema,
            table=table,
        )
        res = self.run_app(
            [
                "settings",
                "non-prod",
                "add",
                database,
                schema,
                table,
                platform.value,
            ]
        )
        assert not res.exit_code

        res = self.run_app(
            [
                "settings",
                "non-prod",
                "get",
            ]
        )
        assert not res.exit_code
        non_prod = GetNonProdSettingsSettingsNonProd.model_validate_json(res.output)
        assert (
            non_prod.dataset_patterns
            and next(
                (
                    pat
                    for pat in non_prod.dataset_patterns
                    if DatasetPatternInput.model_validate(pat.model_dump(by_alias=True))
                    == target_pattern
                ),
                None,
            )
            is not None
        )

        res = self.run_app(
            [
                "settings",
                "non-prod",
                "remove",
                database,
                schema,
                table,
                platform.value,
            ]
        )
        assert not res.exit_code

        res = self.run_app(
            [
                "settings",
                "non-prod",
                "get",
            ]
        )
        assert not res.exit_code
        non_prod = GetNonProdSettingsSettingsNonProd.model_validate_json(res.output)
        assert (
            non_prod.dataset_patterns
            and next(
                (
                    pat
                    for pat in non_prod.dataset_patterns
                    if DatasetPatternInput.model_validate(pat.model_dump(by_alias=True))
                    == target_pattern
                ),
                None,
            )
            is None
        )
