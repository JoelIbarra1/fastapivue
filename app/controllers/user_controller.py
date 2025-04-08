# app/controllers/user_controller.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User
from app.schemas.user import UserCreate

async def get_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()

async def get_user(db: AsyncSession, user_id: int):
    return await db.get(User, user_id)

async def create_user(db: AsyncSession, user: UserCreate):
    new_user = User(**user.dict())
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

async def delete_user(db: AsyncSession, user_id: int):
    user = await db.get(User, user_id)
    if user:
        await db.delete(user)
        await db.commit()
    return user

async def update_user(db: AsyncSession, user_id: int, user_data: UserCreate):
    user = await db.get(User, user_id)
    if not user:
        return None
    for key, value in user_data.dict().items():
        setattr(user, key, value)
    await db.commit()
    await db.refresh(user)
    return user