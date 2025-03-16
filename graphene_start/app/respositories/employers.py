from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.models import Employer
from app.respositories import BaseRepository


class EmployerRepository(BaseRepository):
    async def get_multi(self) -> list[Employer]:
        query = select(Employer)
        query = query.options(selectinload(Employer.jobs))
        result = await self._db.execute(query)
        return list(result.scalars().all())
