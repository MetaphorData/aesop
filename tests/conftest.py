import os
import typing

import loguru
import pytest
import yaml

from aesop.config import DEFAULT_CONFIG_PATH, AesopConfig

PATH = DEFAULT_CONFIG_PATH  # Modify me to use your custom config file!


@pytest.fixture(scope="session")
def _user_config() -> typing.Optional[AesopConfig]:
    if not PATH.exists():
        return None
    with open(PATH) as f:
        loguru.logger.info(f"Using user config: {PATH}")
        config = AesopConfig.model_validate(yaml.safe_load(f.read()))
        return config


@pytest.fixture(scope="session")
def config_file(
    tmp_path_factory: pytest.TempPathFactory,
    _user_config: typing.Optional[AesopConfig],
) -> str:
    config = (
        _user_config
        if _user_config
        else AesopConfig(
            environment=os.environ.get("ENVIRONMENT", ""),
            api_key=os.environ.get("METAPHOR_API_KEY", ""),
        )
    )
    loguru.logger.info(f"Config = {config}")
    path = tmp_path_factory.mktemp("config") / "config.yml"
    with open(path, "w") as file:
        file.write(yaml.safe_dump(config.model_dump()))
    return path.as_posix()
