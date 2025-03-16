from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.models import Job
from app.respositories import BaseRepository


class JobRepository(BaseRepository):
    async def get_multi(self) -> list[Job]:
        query = select(Job)
        query = query.options(selectinload(Job.employer))
        result = await self._db.execute(query)
        return list(result.scalars().all())
