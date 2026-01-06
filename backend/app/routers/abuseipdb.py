from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.abuseipdb_service import fetch_abuseipdb

router = APIRouter(prefix="/abuseipdb", tags=["Threat Intelligence"])

@router.get("/check/{ip}")
def check_ip(ip: str, db: Session = Depends(get_db)):
    data = fetch_abuseipdb(ip, db)
    return {
        "ip": data.ip_address,
        "score": data.abuse_confidence_score,
        "reports": data.total_reports,
        "country": data.country_code,
        "usage_type": data.usage_type
    }
