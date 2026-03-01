from fastapi import FastAPI
from app.routes.performance import router as performance_router

app = FastAPI()
app.include_router(performance_router, prefix="/api")
