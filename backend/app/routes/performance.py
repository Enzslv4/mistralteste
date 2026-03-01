from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.performance import Performance, SessionLocal
from app.schemas.performance import PerformanceCreate
from app.services.wandb_service import log_performance_metrics
from app.services.mistral_service import generate_feedback
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/performance/", response_model=PerformanceCreate)
def create_performance(performance: PerformanceCreate, db: Session = Depends(get_db)):
    db_performance = Performance(**performance.dict())
    db.add(db_performance)
    db.commit()
    db.refresh(db_performance)

    log_performance_metrics(performance.student_id, performance.topic, performance.score, performance.time_spent)
    feedback = generate_feedback(performance.student_id, performance.topic, performance.score)
    print(f"Feedback gerado: {feedback}")

    return db_performance

@router.get("/performance/", response_model=List[PerformanceCreate])
def read_performances(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    performances = db.query(Performance).offset(skip).limit(limit).all()
    return performances
