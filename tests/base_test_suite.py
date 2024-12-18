from functools import cached_property
from typing import Optional, Sequence

import loguru
import pytest
import yaml
from click.testing import Result
from typer.testing import CliRunner

from aesop.app import app
from aesop.commands.common.enums.output_format import OutputFormat
from aesop.config import AesopConfig
from aesop.graphql.generated.client import Client


class BaseTestSuite:
    @pytest.fixture(autouse=True)
    def _setup(self, config_file: str) -> None:
        self._config_file = config_file
        self._runner = CliRunner(mix_stderr=False)
        self._app = app

    @cached_property
    def graphql_client(self) -> Client:
        with open(self._config_file) as f:
            return AesopConfig.model_validate(
                yaml.safe_load(f.read())
            ).get_graphql_client()

    def run_app(
        self,
        arguments: Sequence[str] = [],
        format: Optional[OutputFormat] = None,
        override_config_file: Optional[str] = None,
    ) -> Result:
        if override_config_file:
            loguru.logger.info(f"Override config file: {override_config_file}")

        config_file_arguments = [
            "--no-check-newer-version",
            "--config-file",
            override_config_file if override_config_file else self._config_file,
        ]

        output_arguments = ["--output", format.value] if format else []
        arguments = [
            *config_file_arguments,
            *arguments,
            *output_arguments,
        ]
        return self._runner.invoke(self._app, arguments)
