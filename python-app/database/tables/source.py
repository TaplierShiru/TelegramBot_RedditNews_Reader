from .base import Base

from sqlalchemy import Column, Integer, String, ForeignKey


class Source(Base):
    __tablename__ = "source"
    id = Column(Integer, primary_key=True)
    fetch_from = Column(String())

    def __init__(self, fetch_from: str, id: int = None):
        self.fetch_from = fetch_from
        if id is not None:
            self.id = id

