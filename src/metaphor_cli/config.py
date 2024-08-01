# metaphor_cli/config.py

class Config:
    def __init__(self, api_key: str=None, upload_url: str=None):
        self.api_key = api_key
        self.upload_url = upload_url
