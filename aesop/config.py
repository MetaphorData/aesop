from pathlib import Path
from socket import timeout

import yarl
import httpx
from pydantic import BaseModel, Field, HttpUrl, field_serializer

from aesop.graphql.generated.client import Client

DEFAULT_CONFIG_PATH = Path.home() / ".aesop" / "config.yml"


class AesopConfig(BaseModel):
    url_: HttpUrl = Field(alias="url")
    api_key: str

    @field_serializer("url_")
    def serialize_url(self, url_: HttpUrl) -> str:
        return self.url.human_repr()

    @property
    def url(self) -> yarl.URL:
        return yarl.URL(self.url_.scheme + "://" + (self.url_.unicode_host() or ""))

    def get_graphql_client(self) -> Client:
        # yarl does not care if there's a trailing slash, pydantic url does
        return Client(
            url=(self.url / "api" / "graphql").human_repr(),
            http_client=httpx.Client(
                headers={
                    "X-Api-Key": self.api_key,
                    "Content-Type": "application/json",
                },
                timeout=30,
            ),
        )
