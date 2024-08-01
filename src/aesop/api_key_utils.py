import json
from pathlib import Path
from typing import Optional

CONFIG_FILE = Path.home() / ".aesop"


def load_api_key() -> Optional[str]:
    """Load the API key from the config file."""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
            return str(config.get("api_key"))
    return None


def save_api_key(api_key: str) -> None:
    """Save the API key to the config file."""
    CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump({"api_key": api_key}, f)
