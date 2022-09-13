from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject
from easybroker_client.apiclient import ApiClient


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()
    config.from_yaml('config.yml')

    api_client = providers.Singleton(
        ApiClient,
        api_url=config.api.api_url,
        api_key=config.api.api_key,
    )



