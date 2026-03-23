from fastapi import APIRouter

from app.api.v1.endpoints import evidence, integrations

api_router = APIRouter()
api_router.include_router(integrations.router, prefix="/integrations", tags=["integrations"])
api_router.include_router(evidence.router, prefix="/evidence", tags=["evidence"])
