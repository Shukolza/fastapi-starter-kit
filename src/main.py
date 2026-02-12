from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.api.auth import router as auth_router
from src.db.database import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    # no startup logic
    yield
    await engine.dispose()  # ensuring correct db engine closing


app = FastAPI(lifespan=lifespan)

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])


@app.get("/health", tags=["System"])
async def health():
    return {"status": "ok"}
