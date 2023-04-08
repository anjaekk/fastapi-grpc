from typing import Generator
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy import Table, MetaData
from sqlalchemy import insert, delete
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.engine.reflection import Inspector
import utils

DB_URL = f"postgresql+asyncpg://{utils.DATABASE_URL}"

Base = declarative_base()

engine = create_async_engine(DB_URL, echo=True)

get_session = sessionmaker(class_=AsyncSession, expire_on_commit=False, bind=engine)