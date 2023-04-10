from sqlalchemy import select

from database.config import get_session
from database.models import Comments

async def get_comment():
    async with get_session() as db:
        try:
            obj = await db.execute(select(Comments))
            return obj.scalars().first()
        except Exception as e:
            await db.rollback()
            raise e
        finally:
            await db.close()
