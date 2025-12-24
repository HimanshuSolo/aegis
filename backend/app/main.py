from fastapi import FastAPI

app = FastAPI(
    title="Aegis Backend",
    description="Real-Time DDoS Detection System",
    version="0.1.0"
)


@app.get("/health")
def health():
    return {"status": "running"}