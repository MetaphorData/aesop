import csv
from typing import List, Dict, Any
from rich.console import Console

console = Console()
def validate_data_asset(asset: Dict[str, Any]) -> bool:
    """
    Validates a data asset to ensure it has the required fields for the GraphQL mutation.
    
    Args:
        asset (Dict[str, Any]): A dictionary representing a data asset with a nested structure.
    
    Returns:
        bool: True if the asset is valid, False otherwise.
    """
    required_fields = [
        'isPublished',
        'knowledgeCardInfo',
        'knowledgeCardInfo.detail',
        'knowledgeCardInfo.detail.type',
        'knowledgeCardInfo.anchorEntityId'
    ]
    
    for field in required_fields:
        parts = field.split('.')
        d = asset
        for part in parts:
            if part not in d:
                console.print(f"[bold red]Error: Missing required field '{field}' in data asset.[/bold red]")
                return False
            d = d[part]
    
    return True

def validate_upload_domain(upload_domain: str):
    """
    Validates the upload domain to ensure it is in the correct format.
    
    Args:
        upload_domain (str): The domain name for uploading data assets.
    
    Raises:
        ValueError: If the upload domain is not in the correct format.
    """
    if not upload_domain or upload_domain.endswith('.metaphor.io'):
        raise ValueError("Upload domain must non-empty and not end with '.metaphor.io' it is the part before that")
    
    if not upload_domain.startswith('https://'):
        raise ValueError("Upload domain must start with 'https://'")
    
    if ' ' in upload_domain:
        raise ValueError("Upload domain cannot contain spaces")
    
    if upload_domain.count('.') > 1:
        raise ValueError("Upload domain must contain atmost one period (.)")
    
    if upload_domain.count('/') > 0:
        raise ValueError("Upload domain cannot contain forward slashes (/)")