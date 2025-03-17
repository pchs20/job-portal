from typing import Any

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.models import Job
from app.respositories import BaseRepository


class JobRepository(BaseRepository):
    async def get(self, job_id: int) -> Job | None:
        query = select(Job).where(Job.id == job_id)
        query = query.options(selectinload(Job.employer))
        result = await self._db.execute(query)
        return result.scalars().one_or_none()

    async def get_multi(self) -> list[Job]:
        query = select(Job)
        query = query.options(selectinload(Job.employer))
        result = await self._db.execute(query)
        return list(result.scalars().all())

    async def create(self, job_in: Job) -> Job:
        new_job = Job(
            title=job_in.title,
            description=job_in.description,
            employer_id=job_in.employer_id,
        )
        self._db.add(new_job)
        await self.commit()
        await self._db.refresh(new_job)
        return new_job

    async def update(self, job_id: int, job_in: dict[str, Any]) -> Job | None:
        job = await self.get(job_id)
        if job is None:
            return None
        self.update_model(model=job, update=job_in)
        await self.commit()
        await self._db.refresh(job)
        return job
