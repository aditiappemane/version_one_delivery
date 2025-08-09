# main.py
from fastapi import FastAPI
from .database import engine, Base
from .routers import restaurants

app = FastAPI(title="Restaurant Management API")

# Include routes
app.include_router(restaurants.router)

# Create tables when app starts
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)