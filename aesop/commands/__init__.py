from .aspects import tags_app
from .entities import datasets_app
from .info.info import info as info_command
from .settings.settings import app as settings_app
from .upload.upload import upload as upload_command

__all__ = [
    "upload_command",
    "info_command",
    "settings_app",
    "tags_app",
    "datasets_app",
]
