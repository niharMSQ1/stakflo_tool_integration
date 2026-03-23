import asyncpg
from fastapi import APIRouter, Depends

from app.core.deps import get_db

router = APIRouter()


@router.post("/collect")
async def collect_evidence(conn: asyncpg.Connection = Depends(get_db)):
    """Resolve `evidence_masters`, call tool APIs, write `evidence` + `evidence_collection` + `evidence_mappeds`."""
    return {}
