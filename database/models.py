from .config import Base
from .enums import StatusEnum
from sqlalchemy import Column, String, DateTime, Integer, Enum, Boolean
from sqlalchemy.sql import func


class Comments(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    created = Column(DateTime(timezone=True), default=func.now())
    status = Column(Enum(StatusEnum))
    context = Column(String)