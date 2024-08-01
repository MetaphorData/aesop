# metaphor_cli/data_asset_loaders.py

import csv
from typing import List, Dict, Any
import sys
from rich.console import Console

console = Console()

def load_data_assets_from_csv(csv_path: str) -> List[Dict[str, Any]]:
    """
    Loads data asset information from a CSV file and converts it to a nested structure.
    
    Args:
        csv_path (str): Path to the CSV file.
    
    Returns:
        List[Dict[str, Any]]: A list of dictionaries, where each dictionary represents a data asset
        with a nested structure.
    
    Raises:
        SystemExit: If an error occurs during file reading or if required columns are missing.
    """
    try:
        with open(csv_path, "r") as file:
            reader = csv.DictReader(file)
            
            # Check if required columns exist
            required_columns = ['type', 'knowledgeCardInfo>detail>type', 'knowledgeCardInfo>anchorEntityId']
            missing_columns = [col for col in required_columns if col not in reader.fieldnames]
            if missing_columns:
                console.print(f"[bold red]Error: The CSV file is missing the required column(s): {', '.join(missing_columns)}[/bold red]")
                sys.exit(1)
            
            data_assets = [convert_to_nested_structure(row) for row in reader]
        
        if not data_assets:
            console.print("[bold yellow]Warning: The CSV file is empty.[/bold yellow]")
        
        return data_assets
    
    except FileNotFoundError:
        console.print(f"[bold red]Error: The file '{csv_path}' was not found.[/bold red]")
        sys.exit(1)
    except PermissionError:
        console.print(f"[bold red]Error: Permission denied when trying to read '{csv_path}'.[/bold red]")
        sys.exit(1)
    except csv.Error as e:
        console.print(f"[bold red]Error: An issue occurred while reading the CSV file: {str(e)}[/bold red]")
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
        Dict[str, Any]: A dictionary with a nested structure based on the '>' separators in the keys.
    """
    result = {}
    for key, value in row.items():
        if value.strip() == '':  # Skip empty values
            continue
        parts = key.split('>')
        d = result
        for part in parts[:-1]:
            if part not in d:
                d[part] = {}
            d = d[part]
        d[parts[-1]] = value
    
    # Convert 'isPublished' to boolean
    if 'isPublished' in result:
        result['isPublished'] = result['isPublished'].lower() == 'true'
    
    return result