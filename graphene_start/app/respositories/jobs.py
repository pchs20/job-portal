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
