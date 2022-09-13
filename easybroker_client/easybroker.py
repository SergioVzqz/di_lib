from aiohttp import ClientSession

class EasyBroker:

    def __init__(self, api_url: str, api_key: str) -> None:
        self.api_url = api_url
        self.api_key = api_key

