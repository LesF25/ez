from sqlalchemy.ext.asyncio import AsyncSession

from src.app.domain.repositories.base_repository import AbstractRepository


class SQLAlchemyAbstractRepository(AbstractRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
