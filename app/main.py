from fastapi import FastAPI
from app.api.categories import router as categories_router
from app.api.transactions import router as transactions_router
from app.api.auth import router as auth_router
from app.api.stats import router as stats_router

app = FastAPI(
    title="Finance Tracker API",
    description="Asynchronous REST API for personal finance tracking, category management, and financial analytics.",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(categories_router)
app.include_router(transactions_router)
app.include_router(stats_router)


@app.get("/")
async def root():
    return {"message": "Finance Tracker API is running"}