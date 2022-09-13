from dependecy_injector import containers, providers
from easybroker_client.easybroker import EasyBroker

class ApiClient(containers.DeclarativeContainer):
    api_url = providers.Dependency()
    api_key = providers.Dependency()
    easybroker_api = providers.Singleton(
            EasyBroker,
            api_url = api_url,
            api_key = api_key,
    )