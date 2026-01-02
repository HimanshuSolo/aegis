from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.log_generator import generate_dummy_logs

router = APIRouter(prefix="/simulate", tags=["Simulation"])

@router.post("/logs")
def simulate_logs(db: Session = Depends(get_db), count: int = 50):
    generate_dummy_logs(db, count)
    return {"message": f"Successfully generated {count} dummy logs."}