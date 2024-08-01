import aiohttp
from rich.console import Console
import aiohttp
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from graphql import build_schema

from rich import print as rprint

console = Console()

async def upload_knowledge_card(asset_data: dict, api_key: str, upload_domain: str):
    """
    Uploads a knowledge card to the Metaphor platform using GraphQL.

    This function constructs a dynamic GraphQL mutation based on the provided asset data,
    sends it to the specified Metaphor GraphQL endpoint, and handles the response.

    Args:
        asset_data (dict): A dictionary containing the fields and values of the knowledge card.
        api_key (str): The API key used for authentication with the GraphQL service.
        upload_domain (str): The full domain of the Metaphor GraphQL endpoint.

    Raises:
        Exception: If the upload fails, either due to network problems or server-side issues.
    """
    headers = {"X-Api-Key": f"{api_key}", "Content-Type": "application/json"}
    transport = AIOHTTPTransport(url=f"https://{upload_domain}.metaphor.io/api/graphql", headers=headers)

    with open("schema.gql", "r") as f:
        schema_str = f.read()

    # Parse the schema into a DocumentNode
    schema = build_schema(schema_str)

    mutation, variables = construct_mutation(asset_data)


    async with Client(transport=transport, schema=schema) as session:

        try:
            # Execute the mutation along with local validation
            # local validation done automatically by gql library
            result = await session.execute(mutation, variable_values=variables)
            rprint(f"[green]Knowledge card uploaded successfully with ID: {result['createKnowledgeCard']['id']}[/green]")

        except Exception as e:
            rprint(f"[bold red]Knowledge card upload failed: {e}[/bold red].")

def construct_mutation(asset_data: dict) -> tuple[str, dict]:
    """
    Constructs a GraphQL mutation for uploading a knowledge card based on the provided data.

    This function dynamically generates the mutation string and variable dictionary needed
    to upload a knowledge card using the fields provided in the asset_data dictionary.

    Args:
        asset_data (dict): A dictionary containing the fields and values for the knowledge card.

    Returns:
        tuple: A tuple containing the mutation string and variables dictionary.
    """
    variables = {k: v for k, v in asset_data.items() if k.lower() != 'type'}
    mutation = """
    mutation addKnowledgeCard($input: KnowledgeCardInput!) {
        createKnowledgeCard(data: $input) {
            id
        }
    }
    """
    return gql(mutation), {"input": variables}
