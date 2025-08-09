# food_delivery/create_tables.py
import asyncio
from .database import engine, Base
from . import models

async def create_tables():
    print(f"DB Path: {engine.url.database}")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Tables created successfully!")

if __name__ == "__main__":
    asyncio.run(create_tables())
