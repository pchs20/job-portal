from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.models import JobApplication
from app.respositories import BaseRepository


class JobApplicationRepository(BaseRepository):
    async def get_multi(
        self,
        job_id: int | None = None,
        user_id: int | None = None,
    ) -> list[JobApplication]:
        query = select(JobApplication)
        if job_id is not None:
            query = query.where(JobApplication.job_id == job_id)
        if user_id is not None:
            query = query.where(JobApplication.user_id == user_id)
        query = query.options(selectinload(JobApplication.user))
        query = query.options(selectinload(JobApplication.job))
        result = await self._db.execute(query)
        return list(result.scalars().all())

    async def create(self, job_application: JobApplication) -> JobApplication:
        self._db.add(job_application)
        await self.commit()
        await self._db.refresh(job_application)
        return job_application
