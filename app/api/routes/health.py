from fastapi import APIRouter
from app.core.db import get_db

router = APIRouter(tags=["health"])

@router.get("/health")
def health():
    db = get_db()
    db.command("ping")
    return {"status": "ok", "mongo": "connected"}
