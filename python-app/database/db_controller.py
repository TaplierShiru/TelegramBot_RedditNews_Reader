import traceback
from typing import Optional

from .tables import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(f"sqlite:///database_data/database_newsbot.db", echo=False)
# Create all tables
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


class DataBaseController:

    @staticmethod
    def update_source(fetch_from: str, id: int) -> bool:
        try:
            new_source = Source(fetch_from=fetch_from, id=id)
            session.add(new_source)
            session.commit()
        except Exception:
            traceback.print_exc()
            return False
        return True

    @staticmethod
    def get_source(id: int) -> Optional[Source]:
        try:
            found = session.query(Source).filter_by(id=id).first()
            return found
        except Exception:
            traceback.print_exc()

