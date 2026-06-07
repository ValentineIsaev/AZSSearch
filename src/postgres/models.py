from datetime import datetime
from typing import List

from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

class Capital(Base):
    __tablename__ = 'capital'

    name: Mapped[str]

class GasStation(Base):
    __tablename__ = 'gas_stations'

    name: Mapped[str]
    lat: Mapped[int]
    lot: Mapped[int]
    capital_id: Mapped[int]

class UserMessage(Base):
    __tablename__ = 'user_messages'

    datetime: Mapped[datetime] = mapped_column(default=datetime.now())

    gas_station_id: Mapped[int]

    types_of_fuel: Mapped[List[str]]
    price: Mapped[List[float]]

    queue_lvl: Mapped[int]