# app/routes/user_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import SessionLocal
from app.schemas.user import UserCreate, UserOut
from app.controllers import user_controller

router = APIRouter(prefix="/users", tags=["users"])

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.get("/", response_model=list[UserOut])
async def read_users(db: AsyncSession = Depends(get_db)):
    return await user_controller.get_users(db)

@router.get("/{user_id}", response_model=UserOut)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await user_controller.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=UserOut)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await user_controller.create_user(db, user)

@router.delete("/{user_id}", response_model=UserOut)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await user_controller.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserOut)
async def update_user(user_id: int, user: UserCreate, db: AsyncSession = Depends(get_db)):
    updated_user = await user_controller.update_user(db, user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user