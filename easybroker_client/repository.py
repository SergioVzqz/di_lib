from dependency_injector import containers, providers
from easybroker_client.api_consumtion_repository import ApiConsumtionRepository

class Repository(containers.DeclarativeContainer):
    api_client = providers.DependenciesContainer()

    api_consumtion_repository = providers.Factory(
        ApiConsumtionRepository,
        api_client = api_client
    )
