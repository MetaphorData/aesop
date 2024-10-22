from typing import Optional

from rich import print, print_json
from typer import Context, Typer

from aesop.commands.common.enums.output_format import OutputFormat
from aesop.commands.common.options import OutputFormatOption
from aesop.config import AesopConfig
from aesop.graphql.generated.get_domain import GetDomainNodeNamespace
from aesop.graphql.generated.input_types import NamespaceDescriptionInput

app = Typer()


@app.command()
def add(
    ctx: Context,
    name: str,
    description: Optional[str] = None,
    tokenized_description: Optional[str] = None,
    color: Optional[str] = None,  # hex string
    icon_key: Optional[str] = None,  # hex string
    parent_id: Optional[str] = None,
) -> None:
    config: AesopConfig = ctx.obj
    resp = (
        config.get_graphql_client()
        .create_domain(
            name=name,
            description=NamespaceDescriptionInput(
                text=description,
                tokenizedText=tokenized_description,
            ),
            color=color,
            icon_key=icon_key,
            parent_id=parent_id,
        )
        .create_namespace
    )
    assert resp
    print(f"Created domain: {resp.id}")


@app.command()
def get(
    ctx: Context,
    id: str,
    output_format: OutputFormat = OutputFormatOption,
) -> None:
    config: AesopConfig = ctx.obj
    resp = config.get_graphql_client().get_domain(id).node
    assert isinstance(resp, GetDomainNodeNamespace)
    if output_format is OutputFormat.JSON:
        print_json(resp.model_dump_json())


@app.command()
def remove(
    ctx: Context,
    id: str,
) -> None:
    config: AesopConfig = ctx.obj
    resp = config.get_graphql_client().delete_domain(id).delete_namespaces
    print(resp)
