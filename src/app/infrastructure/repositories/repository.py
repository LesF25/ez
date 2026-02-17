from sqlalchemy.ext.asyncio import AsyncSession

from src.core.domain.repository import AbstractRepository


class SQLAlchemyAbstractRepository(AbstractRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
