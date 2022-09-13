from dependency_injector import containers, providers
from easybroker_client.api_client import ApiClient
from easybroker_client.repository import Repository


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()
    config.from_yaml('config.yml')

    api_client = providers.Singleton(
        ApiClient,
        api_url=config.api.api_url,
        api_key=config.api.api_key,
    )

    repositories = providers.Container(
        Repository,
        api_client,
    )



