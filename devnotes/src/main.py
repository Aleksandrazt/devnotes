"""
Точка входа
"""

from fastapi import FastAPI
from router.main import router

app = FastAPI()
app.include_router(router)
