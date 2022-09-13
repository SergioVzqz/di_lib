from aiohttp import ClientSession

class EasyBroker:
    client_session: any

    def __init__(self, api_url: str, api_key: str) -> None:
        self.api_url = api_url
        self.api_key = api_key
        self.client_session = self.create_session(api_url, api_key)


    async def create_session(self, api_url, api_key):
        pass