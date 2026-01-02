from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database import Base

class CloudflareLog(Base):
    __tablename__ = "cloudflare_logs"

    id = Column(Integer, primary_key=True, index=True)

    ip_address = Column(String, index=True)
    request_path = Column(String)
    status_code = Column(Integer)
    bytes_sent = Column(Integer)

    created_at = Column(DateTime(timezone=True), server_default=func.now())



# ip_address	->   Aggregate traffic by IP
# request_path	->   Detect endpoint abuse
# status_code	->   Error-rate calculation
# bytes_sent	->   Traffic volume
# created_at	->   Time-window aggregation
