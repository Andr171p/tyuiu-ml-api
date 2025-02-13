from dishka import make_async_container

from src.api_v1.providers import ModelServiceProvider


container = make_async_container(
    ModelServiceProvider()
)
