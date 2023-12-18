#!/usr/bin/python3
"""
Esté crea la tabla states en hbtn_0e_6_usa.
"""

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String


class Base(DeclarativeBase):
    """
    Herecia de clase DeclarativeBase
    """
    pass


class State(Base):
    """
    Mapeo de nuestra tabla
    """
    __tablename__ = 'states'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)

    def __repr__(self) -> str:
        """
        Representación formal de nuestra clase.
        """
        return f"states(id={self.id}, name={self.name})"
