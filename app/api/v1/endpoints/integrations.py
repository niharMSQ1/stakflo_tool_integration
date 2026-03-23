import asyncpg
from fastapi import APIRouter, Depends

from app.core.deps import get_db

router = APIRouter()


@router.post("")
async def create_or_update_integration(conn: asyncpg.Connection = Depends(get_db)):
    """Save credentials to `tool_integrations` (step 2)."""
    return {}
