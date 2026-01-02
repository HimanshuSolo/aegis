import random
from datetime import datetime
from sqlalchemy.orm import Session
from app.models.cloudflare_log import CloudflareLog

SUSPICIOUS_PATHS = [
    "/wp-login.php",
    "/admin",
    "/login",
    "/env",
    "/phpmyadmin"
]

NORMAL_PATHS = [
    "/home","/about", "/contact", "/products", "/services", "/blog"
]

def generate_dummy_logs(db: Session, num_logs: int = 1000):
    for _ in range(num_logs):
        ip_address = f"192.168.{random.randint(0, 255)}.{random.randint(0, 255)}"
        if random.random() < 0.1:  
            request_path = random.choice(SUSPICIOUS_PATHS)
        else:
            request_path = random.choice(NORMAL_PATHS)
        
        status_code = random.choices(
            population=[200, 301, 400, 403, 404, 500],
            weights=[0.7, 0.1, 0.05, 0.05, 0.05, 0.05],
            k=1
        )[0]
        
        bytes_sent = random.randint(500, 5000) if status_code == 200 else random.randint(100, 1000)
        
        log = CloudflareLog(
            ip_address=ip_address,
            request_path=request_path,
            status_code=status_code,
            bytes_sent=bytes_sent,
            created_at=datetime.utcnow()
        )
        
        db.add(log)
    
    db.commit()

    