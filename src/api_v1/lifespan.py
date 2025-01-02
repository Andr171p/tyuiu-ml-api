from contextlib import (
    asynccontextmanager,
    AbstractAsyncContextManager
)

from fastapi import FastAPI

from src.s3.bucket import S3Bucket
from src.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AbstractAsyncContextManager[None]:
    s3_bucket = S3Bucket()
    await s3_bucket.download_file(
        object_name="classifier",
        destination_path=settings.ml.clf
    )
    yield
    del s3_bucket
