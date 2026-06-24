from fastapi import FastAPI
from .root_router import root_router

app = FastAPI()

app.include_router(root_router)
