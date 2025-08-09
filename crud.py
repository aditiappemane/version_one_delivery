
# crud.py
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from . import models, schemas

async def create_restaurant(db: AsyncSession, restaurant: schemas.RestaurantCreate):
    new_restaurant = models.Restaurant(**restaurant.dict())
    db.add(new_restaurant)
    try:
        await db.commit()
        await db.refresh(new_restaurant)
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Restaurant name already exists")
    return new_restaurant

async def get_restaurants(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(models.Restaurant).offset(skip).limit(limit))
    return result.scalars().all()

async def get_restaurant(db: AsyncSession, restaurant_id: int):
    result = await db.execute(select(models.Restaurant).where(models.Restaurant.id == restaurant_id))
    restaurant = result.scalar_one_or_none()
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return restaurant

async def update_restaurant(db: AsyncSession, restaurant_id: int, updated_data: schemas.RestaurantUpdate):
    restaurant = await get_restaurant(db, restaurant_id)
    for key, value in updated_data.dict().items():
        setattr(restaurant, key, value)
    await db.commit()
    await db.refresh(restaurant)
    return restaurant

async def delete_restaurant(db: AsyncSession, restaurant_id: int):
    restaurant = await get_restaurant(db, restaurant_id)
    await db.delete(restaurant)
    await db.commit()
    return {"message": "Restaurant deleted"}

async def search_by_cuisine(db: AsyncSession, cuisine: str):
    result = await db.execute(select(models.Restaurant).where(models.Restaurant.cuisine_type.ilike(f"%{cuisine}%")))
    return result.scalars().all()

# crud.py
async def get_active_restaurants(db: AsyncSession):
    result = await db.execute(
        select(models.Restaurant)
        .where(models.Restaurant.is_active == True)
    )
    return result.scalars().all()
