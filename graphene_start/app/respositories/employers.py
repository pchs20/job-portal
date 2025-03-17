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

    async def create(self, employer_in: Employer) -> Employer:
        new_employer = Employer(
            name=employer_in.name,
            contact_email=employer_in.contact_email,
            industry=employer_in.industry,
        )
        self._db.add(new_employer)
        await self.commit()
        await self._db.refresh(new_employer)
        return new_employer
