from .info.info import info as info_command
from .settings.settings import app as settings_app
from .tags.tags import app as tags_app
from .upload.upload import upload as upload_command

__all__ = [
    "upload_command",
    "info_command",
    "tags_app",
    "settings_app",
]
