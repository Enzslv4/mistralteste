from pydantic import BaseModel
from datetime import datetime

class PerformanceCreate(BaseModel):
    student_id: str
    topic: str
    score: float
    time_spent: int
    timestamp: datetime
