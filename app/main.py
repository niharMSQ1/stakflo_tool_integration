from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.config import settings
from app.db.pool import close_pool, create_pool


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_pool()
    yield
    await close_pool()


app = FastAPI(
    title=settings.app_name,
    lifespan=lifespan,
)

app.include_router(api_router, prefix=settings.api_v1_prefix)


@app.get("/health")
async def health():
    return {"status": "ok"}
