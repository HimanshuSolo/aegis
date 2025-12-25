from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database import Base

class ThreatDetection(Base):
    __tablename__ = "threat_detections"

    id = Column(Integer, primary_key=True, index=True)

    ip_address = Column(String, index=True)
    risk_score = Column(Integer)
    prediction = Column(String)

    detected_at = Column(DateTime(timezone=True), server_default=func.now())


# ip_address	->   Identify attacker
# risk_score	->   ML confidence (0–100)
# prediction	->   benign / malicious
# detected_at	->   Audit & visualization