import pytest

from aesop.commands.common.enums.output_format import OutputFormat
from aesop.graphql.generated.get_setup_info import GetSetupInfoSetupInfo
from tests.base_test_suite import BaseTestSuite


class TestInfo(BaseTestSuite):
    @pytest.mark.parametrize(
        "format", [OutputFormat.CSV, OutputFormat.JSON, OutputFormat.TABULAR]
    )
    def test_info(self, format: OutputFormat) -> None:
        res = self.run_app(
            arguments=[
                "info",
            ],
            format=format,
        )
        assert res.exit_code == 0

        if format is OutputFormat.JSON:
            # For JSON, make sure we can validate it
            GetSetupInfoSetupInfo.model_validate_json(res.stdout.replace("'", '"'))
