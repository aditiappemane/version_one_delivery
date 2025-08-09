
# routers/restaurants.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from .. import schemas, crud
from ..database import get_db

router = APIRouter(prefix="/restaurants", tags=["Restaurants"])

@router.post("/", response_model=schemas.RestaurantOut)
async def create_restaurant(restaurant: schemas.RestaurantCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_restaurant(db, restaurant)

@router.get("/", response_model=List[schemas.RestaurantOut])
async def list_restaurants(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await crud.get_restaurants(db, skip, limit)


# routes
@router.get("/active", response_model=List[schemas.RestaurantOut])
async def get_active_restaurants(db: AsyncSession = Depends(get_db)):
    return await crud.get_active_restaurants(db)


@router.get("/{restaurant_id}", response_model=schemas.RestaurantOut)
async def get_restaurant(restaurant_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.get_restaurant(db, restaurant_id)

@router.put("/{restaurant_id}", response_model=schemas.RestaurantOut)
async def update_restaurant(restaurant_id: int, updated_data: schemas.RestaurantUpdate, db: AsyncSession = Depends(get_db)):
    return await crud.update_restaurant(db, restaurant_id, updated_data)

@router.delete("/{restaurant_id}")
async def delete_restaurant(restaurant_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.delete_restaurant(db, restaurant_id)

@router.get("/search/", response_model=List[schemas.RestaurantOut])
async def search_restaurants(cuisine: str, db: AsyncSession = Depends(get_db)):
    return await crud.search_by_cuisine(db, cuisine)


