from .aspects import tags_app
from .documents.documents import app as documents_app
from .documents.glossaries import app as glossaries_app
from .domains.domains import app as domains_app
from .entities import datasets_app
from .info import info as info_command
from .settings.settings import app as settings_app
from .upload.upload import upload as upload_command
from .webhooks import app as webhooks_app

__all__ = [
    "datasets_app",
    "documents_app",
    "domains_app",
    "glossaries_app",
    "info_command",
    "settings_app",
    "tags_app",
    "upload_command",
    "webhooks_app",
]
