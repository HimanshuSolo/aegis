import requests
from datetime import datetime
from sqlalchemy.orm import Session
from app.config import ABUSEIPDB_API_KEY, ABUSEIPDB_BASE_URL
from app.models.abuse_ip import AbuseIP

def fetch_abuseipdbdata(db : Session, ip : str):
    cached = db.query(AbuseIP).filter(AbuseIP.ip_address == ip).first()
    if cached:
        return cached
    
    headers = {
        "Key": ABUSEIPDB_API_KEY,
        "Accept": "application/json"
    }
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }
    response = requests.get(ABUSEIPDB_BASE_URL, headers=headers, params=params, timeout=10)

    response.raise_for_status()
    data = response.json()["data"]

    abuse = AbuseIP(
        ip_address=ip,
        abuse_confidence_score=data["abuseConfidenceScore"],
        total_reports=data["totalReports"],
        country_code=data.get("countryCode"),
        usage_type=data.get("usageType"),
        is_whitelisted=data.get("isWhitelisted"),
        last_reported_at=(
            datetime.fromisoformat(data["lastReportedAt"].replace("Z", ""))
            if data.get("lastReportedAt") else None
    )
 )
    db.add(abuse)
    db.commit()
    db.refresh(abuse)

    return abuse