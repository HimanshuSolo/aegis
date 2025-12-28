from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database import engine, Base
from app.models import cloudflare_log, threat_detection
from app.routers.ingest import router as ingest_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(
    title="Aegis Backend",
    description="Real-Time DDoS Detection System",
    version="0.1.0",
    lifespan=lifespan
)

app.include_router(ingest_router)

@app.get("/health")
def health():
    return {"status": "running"}
