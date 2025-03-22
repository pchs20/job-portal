from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.models import User
from app.respositories import BaseRepository


class UserRepository(BaseRepository):
    async def get(self, user_id: int) -> User | None:
        query = select(User).where(User.id == user_id)
        query = query.options(selectinload(User.job_applications))
        result = await self._db.execute(query)
        return result.scalars().one_or_none()

    async def get_multi(self) -> list[User]:
        query = select(User)
        result = await self._db.execute(query)
        return list(result.scalars().all())
