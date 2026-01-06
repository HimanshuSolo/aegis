import requests
from datetime import datetime
from sqlalchemy.orm import Session
from app.config import ABUSEIPDB_API_KEY, ABUSEIPDB_BASE_URL
from app.models.abuse_ip import AbuseIP

def fetch_abuseipdbdata(db : Session, ip : str):
    cached = db.query(AbuseIP).filter(AbuseIP.ip_address == ip).first()