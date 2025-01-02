import logging
import aiofiles
from typing import Any
from pathlib import Path

from src.s3.client import S3Client
from src.config import settings


log = logging.getLogger(__name__)


class S3Bucket(S3Client):
    def __init__(
            self,
            bucket_name: str = settings.s3.bucket.name
    ) -> None:
        super().__init__()
        self.bucket_name = bucket_name

    async def upload_file(
            self,
            file_path: str | Path,
            object_name: str
    ) -> None:
        async with self.get_client() as client:
            async with aiofiles.open(
                    file=file_path,
                    mode="rb"
            ) as file:
                body: bytes = await file.read()
                await client.put_object(
                    Bucket=self.bucket_name,
                    Key=object_name,
                    Body=body
                )
                log.info("Successfully uploaded file %s", object_name)

    async def download_file(
            self,
            object_name: str,
            destination_path: str | Path
    ) -> None:
        async with self.get_client() as client:
            response = await client.get_object(
                Bucket=self.bucket_name,
                Key=object_name
            )
            log.info("Start download file %s", object_name)
            async with aiofiles.open(
                    file=destination_path,
                    mode="wb"
            ) as file:
                async for chunk in response['Body'].iter_chunks():
                    await file.write(chunk)
                log.info("Successfully download file to %s", destination_path)

    async def delete_file(
            self,
            object_name: str
    ) -> None:
        async with self.get_client() as client:
            await client.delete_object(
                Bucket=self.bucket_name,
                Key=object_name
            )
            log.info("Successfully deleted file %s", object_name)

    async def get_file(
            self,
            object_name: str
    ) -> Any:
        async with self.get_client() as client:
            response = await client.get_object(
                Bucket=self.bucket_name,
                Key=object_name
            )
            body = response["Body"]
            return await body.read()

    async def get_files(self) -> ...:
        ...
