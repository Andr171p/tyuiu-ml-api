from typing import AsyncGenerator, Any
from contextlib import asynccontextmanager

from aiobotocore.client import AioBaseClient
from aiobotocore.session import get_session

from src.config import settings


class S3Client:
    def __init__(
            self,
            access_key: str = settings.s3.access_key,
            secret_key: str = settings.s3.secret_key,
            endpoint_url: str = settings.s3.endpoint_url
    ) -> None:
        self.config = {
            "aws_access_key_id": access_key,
            "aws_secret_access_key": secret_key,
            "endpoint_url": endpoint_url
        }
        self.session = get_session()

    @asynccontextmanager
    async def get_client(self) -> AsyncGenerator[AioBaseClient, Any]:
        async with self.session.create_client("s3", **self.config) as client:
            yield client
