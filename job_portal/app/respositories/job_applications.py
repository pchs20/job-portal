from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.models import JobApplication
from app.respositories import BaseRepository


class JobApplicationRepository(BaseRepository):
    async def get_multi(self) -> list[JobApplication]:
        query = select(JobApplication)
        query = query.options(selectinload(JobApplication.user))
        query = query.options(selectinload(JobApplication.job))
        result = await self._db.execute(query)
        return list(result.scalars().all())
