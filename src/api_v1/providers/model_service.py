from dishka import Provider, Scope, provide

from src.services import ModelService


class ModelServiceProvider(Provider):
    @provide(scope=Scope.APP)
    def get_model_service(self) -> ModelService:
        return ModelService()
