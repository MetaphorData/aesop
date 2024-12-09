from typing import List, Dict, Any, Optional
import typer

from rich import print
from typer import Context, Typer

from aesop.commands.common.exception_handler import exception_handler
from aesop.commands.common.paginator import ClientQueryCallback, paginate_query
from aesop.config import AesopConfig
from aesop.graphql.generated.auto_describe import AutoDescribe


# Define the Typer app
app = typer.Typer(help="Generate descriptions for a dataset in Metaphor.")


@exception_handler("get ai descriptions")
@app.command(help="Batch generates entity descriptions for a specified entity ID.")
def get_ai_descriptions(
    ctx: Context,
    entity_id: str, 
    table: Optional[str] = None, 
    field_paths: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Fetches AI descriptions for a dataset.

    Args:
        entity_id: The ID of the dataset entity.
        table: The name of the table (optional).
        field_paths: A list of field paths (optional).
    
    Returns:
        A dictionary with AI descriptions.
    """
    config: AesopConfig = ctx.obj
    client = config.get_graphql_client()
    # Prepare the variables for the query
    variables = {
        "entity_id": entity_id,
        "table": table,
        "field_paths": field_paths,
        "is_batch": True
    }

    # Execute the query
    query = client.auto_describe(**variables)  # Assuming client.auto_describe returns a query object
    response = query.execute()  # No need to pass the query again, just execute it
    
    # Handle the response
    auto_describe = response.get("autoDescribe", [])
    if not auto_describe:
        raise ValueError(f"No descriptions returned for entity_id={entity_id} and table={table}.")

    result = auto_describe[0] if auto_describe else {}
    return result
