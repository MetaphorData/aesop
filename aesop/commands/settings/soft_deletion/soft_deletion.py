import typer

from aesop.config import AesopConfig
from aesop.console import console
from aesop.graphql.generated.input_types import SettingsInput, SoftDeletionInput

app = typer.Typer(help="Soft deletion settings")


@app.command()
def get(
    ctx: typer.Context,
) -> None:
    config: AesopConfig = ctx.obj
    client = config.get_graphql_client()
    settings = client.get_soft_deletion_settings()
    soft_deletion = settings.settings.soft_deletion
    if not soft_deletion:
        raise ValueError
    console.print(soft_deletion.model_dump())


set_app = typer.Typer()
app.add_typer(set_app, name="set")


@set_app.command()
def enabled(
    ctx: typer.Context,
    enabled: bool,
) -> None:
    config: AesopConfig = ctx.obj
    client = config.get_graphql_client()
    soft_deletion = client.get_soft_deletion_settings().settings.soft_deletion
    if not soft_deletion:
        raise ValueError
    if soft_deletion.enabled is not None and soft_deletion.enabled == enabled:
        console.warning(
            "Not updating: soft deletion already "
            f"{'enabled' if enabled else 'disabled'}"
        )
        return

    client.update_settings(
        input=SettingsInput(
            softDeletion=SoftDeletionInput(
                enabled=enabled, thresholdHours=soft_deletion.threshold_hours
            )
        )
    )
    console.ok("Updated soft deletion settings.")


@set_app.command(name="threshold_hours")
def threshold_hours(
    ctx: typer.Context,
    hours: int = typer.Argument(
        min=0,
    ),
) -> None:
    config: AesopConfig = ctx.obj
    client = config.get_graphql_client()
    client.update_settings(
        input=SettingsInput(
            softDeletion=SoftDeletionInput(
                thresholdHours=hours,
            )
        )
    )
    console.ok("Updated soft deletion settings.")
