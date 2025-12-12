# app/routers/public.py
from fastapi import APIRouter
from starlette.responses import FileResponse
from pathlib import Path

router = APIRouter(tags=["public"])

@router.get("/")
async def index():
    finalPath = Path.cwd() / "frontend" / "index.html"
    print(f"[DEBUG] Serving frontend from {finalPath}")
    return FileResponse(finalPath)

@router.get("/health")
async def health_check():
    print("[DEBUG] Health check requested")
    return {"status": "ok"}
