import asyncio
import csv
from enum import Enum
import sys
from typing import Any, Dict, List

from aesop.commands.common.exception_handler import exception_handler
from aesop.console import console
from aesop.config import AesopConfig
from aesop.generated.base_operation import GraphQLField
from aesop.generated.custom_mutations import Mutation
from aesop.generated.input_types import KnowledgeCardInput


@exception_handler(command="upload", exception_type=Exception)
def upload(csv_path: str, config: AesopConfig):
    asyncio.run(_upload_assets(_load_assets(csv_path), config))
    console.ok("All data assets uploaded successfully.")


async def _upload_assets(data_assets: List[Dict[str, Any]], config: AesopConfig):
    client = config.get_graphql_client()
    for asset in data_assets:
        if isinstance(asset, KnowledgeCardInput):
            mutation = Mutation.create_knowledge_card(data=asset)
            output_fields = [GraphQLField("id")]
            mutation._subfields.extend(output_fields)
            operation_name = "createKnowledgeCard"
            response = await client.mutation(mutation, operation_name=operation_name)
            console.ok(
                f"Data asset with {operation_name} uploaded successfully with ID: {response[operation_name]['id']}"
            )
        else:
            console.warning(f"Skipping asset with unsupported type: {type(asset)}")


class AssetType(str, Enum):
    KNOWLEDGE_CARD = "KNOWLEDGE_CARD"


SUPPORTED_ASSET_TYPES = {
    AssetType.KNOWLEDGE_CARD: KnowledgeCardInput,
}


ASSET_REQUIRED_FIELDS = {
    AssetType.KNOWLEDGE_CARD: [
        "isPublished",
        "knowledgeCardInfo",
        "knowledgeCardInfo.detail",
        "knowledgeCardInfo.detail.type",
        "knowledgeCardInfo.anchorEntityId",
    ]
}


def validate_data_asset(asset: Dict[str, Any], required_fields: List[str]) -> bool:
    for field in required_fields:
        parts = field.split(".")
        d = asset
        for part in parts:
            if part not in d:
                console.error(f"Missing required field '{field}' in data asset.")
                return False
            d = d[part]

    return True


def _load_assets(csv_path: str) -> List[Dict[str, Any]]:
    """
    Loads data asset information from a CSV file and converts it to a nested structure.

    Args:
        csv_path (str): Path to the CSV file.

    Returns:
        List[pydantic_models]: A list of pydantic models, where each model represents a data asset.
    """
    with open(csv_path, "r") as file:
        reader = csv.DictReader(file)

        # Check if 'type' column exists
        if "type" not in reader.fieldnames:
            raise ValueError("Column 'type' is required in CSV header row")

        data_assets = []
        for row in reader:
            raw_type = row.pop("type").upper()  # Remove 'type' from the row
            if raw_type not in AssetType:
                raise ValueError(f"Invalid type: {raw_type}")
            asset_type = AssetType(raw_type)
            if asset_type not in SUPPORTED_ASSET_TYPES:
                console.warning(f"Warning: Unsupported asset type '{raw_type}', skipping this row.")
                continue

            if asset_type not in ASSET_REQUIRED_FIELDS:
                raise NotImplementedError

            model_class = SUPPORTED_ASSET_TYPES[asset_type]
            try:
                data_asset_nested = _convert_to_nested_structure(row)

                # Need to check for required fields else upload will fail
                # This is not done by pydantic models generated from the schema
                # The models only validate the fields that are present
                if not validate_data_asset(data_asset_nested, ASSET_REQUIRED_FIELDS[asset_type]):
                    continue
                data_assets.append(model_class.model_validate(data_asset_nested))
            except Exception as e:
                console.warning(f"Cannot parse row = {row}, error = {str(e)}")

    if not data_assets:
        console.warning(("The CSV file is empty or contains no parsable data assets."))

    return data_assets


def _convert_to_nested_structure(row: Dict[str, str]) -> Dict[str, Any]:
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
