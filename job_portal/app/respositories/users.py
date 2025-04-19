from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.models import User
from app.respositories import BaseRepository
from app.security import verify_password


class UserRepository(BaseRepository):
    async def get(self, user_id: int) -> User | None:
        query = select(User).where(User.id == user_id)
        query = query.options(selectinload(User.job_applications))
        result = await self._db.execute(query)
        return result.scalars().one_or_none()

    async def get_by_email(self, email: str) -> User | None:
        query = select(User).where(User.email == email)
        result = await self._db.execute(query)
        return result.scalars().one_or_none()

    async def get_multi(self) -> list[User]:
        query = select(User)
        result = await self._db.execute(query)
        return list(result.scalars().all())

    async def create(self, user: User) -> User:
        self._db.add(user)
        await self.commit()
        await self._db.refresh(user)
        return user

    async def authenticate(
        self,
        email: str,
        password: str,
    ) -> User | None:
        user = await self.get_by_email(email=email)
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return user
