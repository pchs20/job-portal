from __future__ import annotations

from typing import Any

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import Base


class BaseRepository:
    _instance = None

    def __new__(
        cls,
        db: AsyncSession,
    ) -> BaseRepository:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._db = db
        return cls._instance

    async def commit(self):
        try:
            await self._db.commit()
        except IntegrityError:
            await self._db.rollback()
            raise

    @staticmethod
    def update_model(model: Base, update: dict[str, Any]):
        for field, value in update.items():
            setattr(model, field, value)
        return model
