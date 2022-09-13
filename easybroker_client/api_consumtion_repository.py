from dependency_injector import containers, providers

class ApiConsumtionRepository():

    def __init__(self, api_client):
        self.api_client = api_client.client_session

    async def get():
        pass

    async def post():
        pass

    async def patch():
        pass