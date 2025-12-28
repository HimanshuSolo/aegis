from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.cloudflare_log import CloudflareLog
from app.schemas.log_schema import cloudflarelog

router = APIRouter(prefix="/logs", tags=["Logs"])

@router.post("/ingest")
def ingest_log(
    log: cloudflarelog,
    db: Session = Depends(get_db)
):
    db_log = CloudflareLog(
        ip_address=log.ip_address,
        request_path=log.request_path,
        status_code=log.status_code,
        bytes_sent=log.bytes_sent
    )

    db.add(db_log)
    db.commit()
    db.refresh(db_log)

    return {
        "message": "Log ingested successfully",
        "id": db_log.id
    }
