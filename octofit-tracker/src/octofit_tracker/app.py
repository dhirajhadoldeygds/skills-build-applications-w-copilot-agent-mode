from fastapi import FastAPI
from .routers import health

app = FastAPI(title="OctoFit Tracker API")

app.include_router(health.router, prefix="/api")
