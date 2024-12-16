from typing import List, Optional
import typer
import csv
import os

from rich import print
from typer import Context

from aesop.commands.common.exception_handler import exception_handler

from aesop.config import AesopConfig


# Define the Typer app
app = typer.Typer(help="Generate descriptions for a dataset in Metaphor.")


@exception_handler("get ai descriptions")
@app.command(help="Batch generates entity descriptions for entity IDs from a CSV and outputs another CSV in specified directory.")
def get_ai_descriptions(
    ctx: Context,
    input_csv: str,  # Path to the input CSV file
    output_dir: str = "~/Desktop",  # Directory to save the output CSV file
    table: Optional[str] = None, 
    field_paths: Optional[List[str]] = None
) -> None:
    """
    Generates AI descriptions for dataset(s).

    Args:
        input_csv: Path to the input CSV file containing entity IDs.
        output_dir: Directory to save the output CSV file.
        table: The name of the table (optional).
        field_paths: A list of field paths (optional).
    """
    try:
        # Read entity IDs from the input CSV
        with open(input_csv, mode='r', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            entities = [row for row in csvreader]  # Assuming entity IDs are in the first column
    except Exception as e:
        print(f"Error: Failed to read entity IDs from CSV. {e}")
        raise e

    config: AesopConfig = ctx.obj
    client = config.get_graphql_client()

    query = []
    for i in entities[0]:
        variables = {
            "entity_id": i,
            "table": table,
            "field_paths": field_paths,
            "is_batch": True
        }
        query.append(client.auto_describe(**variables)) 

    descriptions = []
    for i, v in enumerate(entities[0]):
        description = {"entity_id": v, "description": query[i].auto_describe[0].description}
        for y in query[i].auto_describe[0].field_descriptions:
            description[y.field_path] = y.field_description
        descriptions.append(description)

    # Determine the output file path
    if output_dir == "~/Desktop":
        default_output = os.path.expanduser(output_dir)  # Expand '~' to the full path
        output_file_path = os.path.join(default_output, 'descriptions_output.csv')
    elif os.path.isdir(output_dir):
        output_file_path = os.path.join(output_dir, 'descriptions_output.csv')
    else:
        print(f"Error: The provided output path is not a directory.")
        return

    # Write descriptions to the output CSV
    all_keys = set()
    for record in descriptions:
        all_keys.update(record.keys())

    try:
        with open(output_file_path, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for entry in descriptions:
                for key, value in entry.items():
                    writer.writerow([key, value])
                writer.writerow([])  # Add a blank line between records
        print(f"Descriptions have been written to {output_file_path}")
    except Exception as e:
        print(f"Error: Failed to write descriptions to CSV. {e}")
        raise e
