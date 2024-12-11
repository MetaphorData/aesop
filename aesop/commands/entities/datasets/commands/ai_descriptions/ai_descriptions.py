import json
from typing import List, Dict, Any, Optional
import typer

from rich import print
from typer import Context, Typer

from aesop.commands.common.exception_handler import exception_handler

from aesop.config import AesopConfig


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
    try:
        entities = json.loads(entity_id)  # Convert the JSON string to a Python list
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse entity_ids as a list. Received: {entity_id}")
        raise e


    config: AesopConfig = ctx.obj
    client = config.get_graphql_client()

    query = []
    for i in entities:
        variables = {
            "entity_id": i,
            "table": table,
            "field_paths": field_paths,
            "is_batch": True
        }
        query.append(client.auto_describe(**variables)) 

    
    descriptions = {}
    for i,v in enumerate(entities):
        descriptions[f"{v}_description"] = query[i].auto_describe[0].description
        for y in query[i].auto_describe[0].field_descriptions:
            descriptions[f"{v}_{y.field_path}"] = y.field_description


    return print(descriptions)
