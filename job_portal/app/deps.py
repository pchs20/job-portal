from typing import Type, TypeVar

from app.database import async_session
from app.respositories import BaseRepository


Repository = TypeVar('Repository', bound=BaseRepository)


async def get_repository(repo_type: Type[Repository]) -> Repository:
    """Factory function to create repository instances."""
    async with async_session() as session:
        return repo_type(session)
