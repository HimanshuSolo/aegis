from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from app.database import Base

class AbuseIP(Base):
    __tablename__ = "abuse_ip_cache"

    id = Column(Integer, primary_key=True)
    ip_address = Column(String, unique=True, index=True)

    abuse_confidence_score = Column(Integer)
    total_reports = Column(Integer)
    country_code = Column(String)
    usage_type = Column(String)
    is_whitelisted = Column(Boolean)

    last_reported_at = Column(DateTime)
    fetched_at = Column(DateTime(timezone=True), server_default=func.now())

# ip_address              ->   IP being checked
# abuse_confidence_score  ->   Confidence score (0–100)
# total_reports           ->   Total number of reports
# country_code            ->   Country code of the IP
# usage_type              ->   Usage type of the IP
# is_whitelisted          ->   Whether the IP is whitelisted
# last_reported_at        ->   Timestamp of the last report
# fetched_at              ->   Timestamp when the data was fetched