from typing import List, Optional

from sqlalchemy import select, update, delete

from .models import User
from .database import database


async def create_user(user: User):
    query = User.__table__.insert().values(
        name=user.name,
        email=user.email,
        password=user.password
    )
    return await database.execute(query)


async def get_users(skip: int = 0, limit: int = 100) -> List[User]:
    query = select(User).offset(skip).limit(limit)
    return await database.fetch_all(query)


async def get_user_by_email(email: str) -> Optional[User]:
    query = select(User).where(User.email == email)
    return await database.fetch_one(query)


async def update_user(user: User):
    query = update(User).where(User.id == user.id).values(
        name=user.name,
        email=user.email,
        password=user.password
    )
    return await database.execute(query)


async def delete_user(user_id: int):
    query = delete(User).where(User.id == user_id)
    return await database.execute(query)
