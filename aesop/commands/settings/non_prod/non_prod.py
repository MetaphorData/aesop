import json

import typer

from aesop.commands.common.all_platforms import ALL_PLATFORMS
from aesop.config import AesopConfig
from aesop.console import console
from aesop.graphql.generated.input_types import (
    DatasetPatternInput,
    NonProdInput,
    SettingsInput,
)

app = typer.Typer(help="Non-prod settings")


@app.command()
def get(
    ctx: typer.Context,
) -> None:
    config: AesopConfig = ctx.obj
    client = config.get_graphql_client()
    settings = client.get_non_prod_settings()
    non_prod = settings.settings.non_prod
    if not non_prod:
        raise ValueError
    console.print(non_prod.model_dump())


def _validate_dataset_pattern_input(
    value: str,
) -> str:
    obj = json.loads(value)
    if "platform" in obj and obj["platform"] not in ALL_PLATFORMS:
        raise typer.BadParameter(
            f"Invalid platform: {obj['platform']}. Valid platforms are: {ALL_PLATFORMS}"
        )
    DatasetPatternInput.model_validate_json(value)
    return value


@app.command()
def set(
    ctx: typer.Context,
    input: str = typer.Argument(
        help="A JSON representing the non prod pattern to set to.",
        callback=_validate_dataset_pattern_input,
    ),
) -> None:
    config: AesopConfig = ctx.obj
    client = config.get_graphql_client()
    client.update_settings(
        input=SettingsInput(
            nonProd=NonProdInput(
                datasetPatterns=[DatasetPatternInput.model_validate_json(input)]
            )
        )
    )
    console.ok("Updated non-prod settings.")
