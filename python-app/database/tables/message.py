from .base import Base

from sqlalchemy import Column, Integer, String, ForeignKey, Date


class Message(Base):
    __tablename__ = "message"
    id = Column(Integer, primary_key=True)
    send_to_id = Column(Integer)
    send_message = Column(String())
    send_time = Column(Date())

    def __init__(self, send_to_id: id, send_message: str, send_time: str, id: int = None):
        self.send_to_id = send_to_id
        self.send_message = send_message
        self.send_time = send_time
        if id is not None:
            self.id = id

