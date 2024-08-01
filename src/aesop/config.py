# Config for upload
from typing import Optional

from pydantic import validator
from pydantic.dataclasses import dataclass

from aesop.input_validation import validate_upload_domain


@dataclass
class BaseConfig:
    api_key: Optional[str] = None


@dataclass
class UploadConfig(BaseConfig):
    upload_domain: Optional[str] = None

    _validate_domain = validator("upload_domain", allow_reuse=True)(validate_upload_domain)
