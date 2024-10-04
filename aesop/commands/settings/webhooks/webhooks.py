from typing import Optional

from rich import print_json
from typer import Argument, Context, Typer

from aesop.config import AesopConfig
from aesop.graphql.generated.enums import WebhookTriggerType

app = Typer(help="Manages webhooks")


@app.command(help="Registers a webhook to Metaphor.")
def register(
    ctx: Context,
    trigger: WebhookTriggerType = Argument(help="The wewbhook trigger type."),
    url: str = Argument(
        "The url for the webhook. Metaphor will send a POST request to this URL."
    ),
) -> None:
    config: AesopConfig = ctx.obj
    print_json(
        config.get_graphql_client()
        .add_webhook(trigger, url)
        .add_webhook.model_dump_json()
    )


@app.command(help="Unregisters a webhook from Metaphor.")
def unregister(
    ctx: Context,
    webhook_id: str = Argument("The ID of the webhook to unregister."),
) -> None:
    config: AesopConfig = ctx.obj
    print_json(
        config.get_graphql_client()
        .remove_webhook(webhook_id)
        .delete_webhooks.model_dump_json()
    )


@app.command(help="Gets a list of webhooks that are registered to Metaphor.")
def get(
    ctx: Context,
    trigger: Optional[WebhookTriggerType] = Argument(default=None),
) -> None:
    config: AesopConfig = ctx.obj
    print_json(config.get_graphql_client().get_webhooks(trigger).model_dump_json())


@app.command(help="Gets the payload of a webhook trigger type.")
def get_payload_schema(
    ctx: Context,
    trigger: WebhookTriggerType = Argument(help="The trigger type."),
) -> None:
    config: AesopConfig = ctx.obj
    print_json(
        config.get_graphql_client()
        .get_webhook_payload_schema(trigger)
        .webhook_payload_schema
    )
