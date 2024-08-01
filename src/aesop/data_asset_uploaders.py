import asyncio
import sys

from rich.console import Console

from aesop.config import UploadConfig
from aesop.data_asset_loaders import load_data_assets_from_csv
from aesop.graphql_models_generated.base_operation import GraphQLField
from aesop.graphql_models_generated.client import Client
from aesop.graphql_models_generated.custom_mutations import Mutation
from aesop.graphql_models_generated.input_types import KnowledgeCardInput

console = Console()


def perform_upload(csv_path: str, api_key: str, upload_domain: str):
    """
    Common function to handle the upload process for all data assets.

    Args:
        csv_path (str): Path to the CSV file containing data assets.
        api_key (str): API key for authentication.
        upload_domain (str): Domain for uploading data assets.
    """
    config = UploadConfig(api_key=api_key, upload_domain=upload_domain)
    try:
        data_assets_upload = load_data_assets_from_csv(csv_path)

        asyncio.run(upload_assets(data_assets_upload, config))
        console.print("[green]All data assets uploaded successfully.[/green]")
    except Exception as e:
        console.print(f"[bold red]An error occurred: {str(e)}[/bold red]")
        raise sys.exit(1)


async def upload_assets(data_assets, config):
    """
    Upload multiple data assets to the Metaphor platform.

    Args:
        data_assets (List[BaseModel]): List of data assets input models to upload.
        config (UploadConfig): Configuration for the upload process.
    """
    client = Client(
        url=f"https://{config.upload_domain}.metaphor.io/api/graphql",
        headers={"X-Api-Key": f"{config.api_key}", "Content-Type": "application/json"},
    )
    for asset in data_assets:
        if isinstance(asset, KnowledgeCardInput):
            mutation = Mutation.create_knowledge_card(data=asset)
            output_fields = [GraphQLField("id")]
            mutation._subfields.extend(output_fields)
            await upload_data_asset(mutation, client, operation_name="createKnowledgeCard")
        else:
            console.print(f"[yellow]Skipping asset with unsupported type: {type(asset)}[/yellow]")


async def upload_data_asset(mutation: GraphQLField, client: Client, operation_name: str):
    """
    Uploads a data asset to the Metaphor platform using GraphQL.

    This function constructs a dynamic GraphQL mutation based on the provided asset data,
    sends it to the specified Metaphor GraphQL endpoint, and handles the response.

    Args:
        mutation (GraphQLField): The GraphQL mutation for uploading the asset.
        client (Client): The GraphQL client instance.

    Raises:
        Exception: If the upload fails, either due to network problems or server-side issues.
    """
    # Execute the mutation
    # validation already done by the pydantic models
    try:
        response = await client.mutation(mutation, operation_name=operation_name)
        console.print(
            (
                f"[green]Data asset with {operation_name} uploaded successfully "
                f"with ID: {response[operation_name]['id']}[/green]"
            )
        )
    except Exception as e:
        console.print(
            (
                f"[bold red]Error uploading data asset "
                f"with operation {operation_name}: {str(e)}[/bold red]"
            )
        )
        raise e
