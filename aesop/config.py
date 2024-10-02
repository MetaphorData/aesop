from pathlib import Path

import yarl
from pydantic import BaseModel

from aesop.graphql.generated.client import Client

DEFAULT_CONFIG_PATH = Path.home() / ".aesop" / "config.yml"


class AesopConfig(BaseModel):
    domain: str
    api_key: str

    @property
    def base_url(self) -> yarl.URL:
        return yarl.URL(f"https://{self.domain}.metaphor.io")

    def get_graphql_client(self) -> Client:
        return Client(
            url=(self.base_url / "api" / "graphql").human_repr(),
            headers={
                "X-Api-Key": self.api_key,
                "Content-Type": "application/json",
            },
        )
