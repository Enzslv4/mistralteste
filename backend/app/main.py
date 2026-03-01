from fastapi import FastAPI
from app.routes import performance, recommendations

app = FastAPI()

app.include_router(performance.router, prefix="/performance")
app.include_router(recommendations.router, prefix="/recommendations")
