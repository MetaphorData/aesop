from typing import List, Optional

import typer
from rich import print, print_json

from aesop.commands.common.arguments import InputFileArg
from aesop.commands.common.exception_handler import exception_handler
from aesop.commands.settings.non_prod.models import BatchSetNonProdInput
from aesop.config import AesopConfig
from aesop.graphql.generated.enums import DataPlatform
from aesop.graphql.generated.get_non_prod_settings import (
    GetNonProdSettingsSettingsNonProd,
)
from aesop.graphql.generated.input_types import (
    DatasetPatternInput,
    NonProdInput,
    SettingsInput,
)

app = typer.Typer(help="Non-prod settings")


def _get_non_prod(
    ctx: typer.Context,
) -> GetNonProdSettingsSettingsNonProd:
    config: AesopConfig = ctx.obj
    client = config.get_graphql_client()
    settings = client.get_non_prod_settings()
    non_prod = settings.settings.non_prod
    if not non_prod:
        raise ValueError
    return non_prod


@exception_handler("Get non prod")
@app.command(help="Gets the non-prod dataset patterns")
def get(
    ctx: typer.Context,
) -> None:
    non_prod = _get_non_prod(ctx)
    print_json(non_prod.model_dump_json())


def _update_dataset_patterns(
    ctx: typer.Context,
    patterns: List[DatasetPatternInput],
) -> None:
    config: AesopConfig = ctx.obj
    config.get_graphql_client().update_settings(
        input=SettingsInput(nonProd=NonProdInput(datasetPatterns=patterns))
    )


@exception_handler("Set non prod")
@app.command(help="Batch updates all non-prod dataset patterns.")
def set(
    ctx: typer.Context, input: typer.FileText = InputFileArg(BatchSetNonProdInput)
) -> None:
    patterns = BatchSetNonProdInput.model_validate_json(input.read()).dataset_patterns
    _update_dataset_patterns(ctx, patterns)


@exception_handler("Add non prod")
@app.command(help="Adds a non-prod dataset pattern.")
def add(
    ctx: typer.Context,
    database: str,
    schema: str,
    table: str,
    platform: DataPlatform,
    account: Optional[str] = None,
    is_case_sensitive: bool = False,
) -> None:
    existing_patterns = [
        DatasetPatternInput(
            account=pat.account,
            database=pat.database,
            isCaseSensitive=pat.is_case_sensitive,
            platform=pat.platform,
            schema=pat.schema_,
            table=pat.table,
        )
        for pat in _get_non_prod(ctx).dataset_patterns
    ]
    new_pattern = DatasetPatternInput(
        account=account,
        database=database,
        isCaseSensitive=is_case_sensitive,
        platform=platform,
        schema=schema,
        table=table,
    )
    if next((pat for pat in existing_patterns if pat == new_pattern), None):
        # The pattern already exists, not updating
        print("The pattern already exists, not updating")
        return
    _update_dataset_patterns(ctx, [*existing_patterns, new_pattern])
    print("Added non-prod pattern.")


@exception_handler("remove non prod")
@app.command(help="Removes a non-prod dataset pattern.")
def remove(
    ctx: typer.Context,
    database: str,
    schema: str,
    table: str,
    platform: DataPlatform,
    account: Optional[str] = None,
    is_case_sensitive: bool = False,
) -> None:
    existing_patterns = [
        DatasetPatternInput(
            account=pat.account,
            database=pat.database,
            isCaseSensitive=pat.is_case_sensitive,
            platform=pat.platform,
            schema=pat.schema_,
            table=pat.table,
        )
        for pat in _get_non_prod(ctx).dataset_patterns
    ]
    target = DatasetPatternInput(
        account=account,
        database=database,
        isCaseSensitive=is_case_sensitive,
        platform=platform,
        schema=schema,
        table=table,
    )

    should_update = False
    patterns: List[DatasetPatternInput] = []
    for pat in existing_patterns:
        if pat != target:
            patterns.append(pat)
        else:
            should_update = True

    if not should_update:
        # This pattern does not exist, not updating
        print("The pattern does not exist, not updating")
        return
    _update_dataset_patterns(ctx, patterns)
    print("Removed non-prod pattern.")
