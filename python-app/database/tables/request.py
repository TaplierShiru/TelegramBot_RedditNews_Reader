from .base import Base

from sqlalchemy import Column, Integer, String, ForeignKey, Date


class Request(Base):
    __tablename__ = "request"
    id = Column(Integer, primary_key=True)
    from_id = Column(Integer)
    request_text = Column(String())
    received_time = Column(Date())
    fetch_from = Column(String())

    def __init__(self, from_id: id, request_text: str, received_time: str, id: int = None):
        self.from_id = from_id
        self.request_text = request_text
        self.received_time = received_time
        if id is not None:
            self.id = id

