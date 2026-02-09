from fastapi import FastAPI
from app.api.routes.health import router as health_router
from app.api.routes.cv import router as cv_router
from app.api.routes.analyze import router as analyze_router

app = FastAPI(title="CV Analyzer API")

app.include_router(health_router)
app.include_router(cv_router)
app.include_router(analyze_router)
