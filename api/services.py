from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.config import get_session
from database.models import Comments

async def get_user():
    async with get_session() as db:
        obj = await db.execute(select(Comments))
