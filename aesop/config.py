from pathlib import Path
from typing import Optional

import yarl
from pydantic import BaseModel

from aesop.graphql.generated.client import Client

DEFAULT_CONFIG_PATH = Path.home() / ".aesop" / "config.yml"


class AesopConfig(BaseModel):
    config: str
    api_key: str
    tenant: Optional[str] = None

    @property
    def base_url(self) -> yarl.URL:
        prefix = f"{self.tenant}.{self.config}" if self.tenant else self.config
        return yarl.URL(f"https://{prefix}.metaphor.io")

    def get_graphql_client(self) -> Client:
        return Client(
            url=(self.base_url / "api" / "graphql").human_repr(),
            headers={
                "X-Api-Key": self.api_key,
                "Content-Type": "application/json",
            },
        )
