from typing import Optional, Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from .models import Base, GasStation, Capital, UserMessage

class BaseRepo:
    def __init__(self, session: AsyncSession, model: Type[Base]):
        self._session = session
        self._model = model

    async def get_by_id(self, id_: int) -> Optional[Type[Base]]:
        stmt = select(self._model).where(
            self._model.id == id_
        )

        result = await self._session.execute(stmt)

        return result.scalar()

    async def delete_by_id(self, id_: int) -> bool:pass

    async def get_all(self) -> tuple[Base]:pass


class GasStationRepo(BaseRepo):
    def __init__(self, session: AsyncSession):
        super().__init__(session, GasStation)

    def create_gas_station(self, station: GasStation):pass

    def get_gas_stations_of_capital(self, capital_id: int):pass