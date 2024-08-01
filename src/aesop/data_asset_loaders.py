import csv
import sys
from typing import Any, Dict, List

from rich.console import Console

from aesop.graphql_models_generated.input_types import KnowledgeCardInput
from aesop.input_validation import validate_data_asset

console = Console()

SUPPORTED_DATA_ASSETS = {
    "KNOWLEDGE_CARD": KnowledgeCardInput,
    # More data assets to be added here
}


def load_data_assets_from_csv(csv_path: str) -> List[Dict[str, Any]]:
    """
    Loads data asset information from a CSV file and converts it to a nested structure.

    Args:
        csv_path (str): Path to the CSV file.

    Returns:
        List[pydantic_models]: A list of pydantic models, where each model represents a data asset.

    Raises:
        SystemExit: If an error occurs during file reading or if required columns are missing.
    """
    try:
        with open(csv_path, "r") as file:
            reader = csv.DictReader(file)

            # Check if 'type' column exists
            if "type" not in reader.fieldnames:
                console.print(
                    "[bold red]Error: The CSV file is missing the required column 'type'[/bold red]"
                )
                sys.exit(1)

            data_assets = []
            for row in reader:
                asset_type = row.pop("type").upper()  # Remove 'type' from the row
                if asset_type not in SUPPORTED_DATA_ASSETS:
                    console.print(
                        (
                            f"[bold yellow]Warning: Unsupported asset type '{asset_type}'."
                            "Skipping this row.[/bold yellow]"
                        )
                    )
                    continue

                model_class = SUPPORTED_DATA_ASSETS.get(asset_type)
                try:
                    data_asset_nested = convert_to_nested_structure(row)

                    # Need to check for required fields else upload will fail
                    # This is not done by pydantic models generated from the schema
                    # The models only validate the fields that are present
                    if not validate_data_asset(data_asset_nested):
                        continue
                    data_assets.append(model_class.model_validate(data_asset_nested))
                except Exception as e:
                    console.print(f"[bold red]Error parsing row: {row}, Error: {e}[/bold red]")

        if not data_assets:
            console.print(
                (
                    "[bold yellow]Warning: The CSV file is empty or contains "
                    "no parsable data assets.[/bold yellow]"
                )
            )

        return data_assets

    except FileNotFoundError:
        console.print(f"[bold red]Error: The file '{csv_path}' was not found.[/bold red]")
        sys.exit(1)
    except PermissionError:
        console.print(
            f"[bold red]Error: Permission denied when trying to read '{csv_path}'.[/bold red]"
        )
        sys.exit(1)
    except csv.Error as e:
        console.print(
            f"[bold red]Error: An issue occurred while reading the CSV file: {str(e)}[/bold red]"
        )
        sys.exit(1)
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred: {str(e)}[/bold red]")
        sys.exit(1)


def convert_to_nested_structure(row: Dict[str, str]) -> Dict[str, Any]:
    """
    Converts a flattened dictionary with keys separated by '>' into a nested dictionary structure.

    Args:
        row (Dict[str, str]): A dictionary representing a flattened data structure.

    Returns:
        Dict[str, Any]: A dictionary with nested structure based on the '>' separators in the keys.
    """
    result = {}
    for key, value in row.items():
        if value.strip() == "":  # Skip empty values
            continue
        parts = key.split(">")
        d = result
        for part in parts[:-1]:
            if part not in d:
                d[part] = {}
            d = d[part]
        d[parts[-1]] = value
    return result
