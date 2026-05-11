from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.core.config import settings
from app.database.database import db_manager

from app.routes import tasks
from app.routes import auth

print("VALOR REAL DO MONGO:", repr(settings.MONGODB_URL))


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Connect to DB
    db_manager.connect()
    yield
    # Shutdown: Close DB
    db_manager.close()


app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


# Register routes
app.include_router(tasks.router, prefix=settings.API_V1_STR)
app.include_router(auth.router, prefix=settings.API_V1_STR)


@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "project": settings.PROJECT_NAME
    }