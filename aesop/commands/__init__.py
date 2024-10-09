from .aspects import custom_metadata_app, tags_app
from .entities import datasets_app
from .info.info import info as info_command
from .settings.settings import app as settings_app
from .upload.upload import upload as upload_command
from .webhooks.webhooks import app as webhooks_app

__all__ = [
    "upload_command",
    "custom_metadata_app",
    "info_command",
    "settings_app",
    "tags_app",
    "datasets_app",
    "webhooks_app",
]
