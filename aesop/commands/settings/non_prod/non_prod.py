import typer

from aesop.commands.common.exception_handler import exception_handler
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


@exception_handler("Set non-prod config")
def _validate_dataset_pattern_input(
    value: str,
) -> str:
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
