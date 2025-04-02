from sqlalchemy import delete, select
from sqlalchemy.orm import selectinload

from app.models import Employer
from app.respositories import BaseRepository


class EmployerRepository(BaseRepository):
    async def get(self, employer_id: int) -> Employer | None:
        query = select(Employer).where(Employer.id == employer_id)
        query = query.options(selectinload(Employer.jobs))
        result = await self._db.execute(query)
        return result.scalars().one_or_none()

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

    async def update(self, employer_id: int, employer_in: dict) -> Employer | None:
        employer = await self.get(employer_id)
        if employer is None:
            return None
        self.update_model(model=employer, update=employer_in)
        await self.commit()
        await self._db.refresh(employer)
        return employer

    async def delete(self, employer_id: int) -> None:
        query = delete(Employer).where(Employer.id == employer_id)
        await self._db.execute(query)
        await self.commit()
