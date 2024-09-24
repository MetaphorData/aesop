from pathlib import Path

import yaml

from tests.base_test_suite import BaseTestSuite


class TestMainCallback(BaseTestSuite):
    def test_help(self) -> None:
        res = self.run_app(["--help"])
        assert res.exit_code == 0

    def test_bad_config_empty_file(self, tmp_path: Path) -> None:
        empty = tmp_path / "empty.yml"
        empty.touch()
        res = self.run_app(["info"], override_config_file=empty.as_posix())
        assert res.exit_code != 0
        assert (
            "Input should be a valid dictionary or instance of AesopConfig"
            in res.stdout
        )

    def test_bad_config_missing_api_key(self, tmp_path: Path) -> None:
        bad_config = tmp_path / "bad_config.yml"
        with open(bad_config, "w") as f:
            config = {
                "config": "bad",
            }
            f.write(yaml.safe_dump(config))
        res = self.run_app(["info"], override_config_file=bad_config.as_posix())
        assert res.exit_code != 0
        assert "Field required" in res.stdout
