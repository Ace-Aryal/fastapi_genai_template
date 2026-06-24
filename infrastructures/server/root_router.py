from fastapi import APIRouter

root_router = APIRouter()
from modules.auth.routes.auth_index import router as auth_router

root_router.include_router(auth_router, prefix="/auth", tags=["auth"])
