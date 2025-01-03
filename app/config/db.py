from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os
from collections.abc import AsyncGenerator


load_dotenv()
Base = declarative_base()

# Use async engine for PostgreSQL
DB_URL = f"postgresql+asyncpg://{os.getenv('PG_USER')}:{os.getenv('PG_PASSWORD')}@{os.getenv('PG_HOST')}:{os.getenv('PG_PORT')}/{os.getenv('PG_DATABASE')}"

# Create an asynchronous engine
engine = create_async_engine(DB_URL, echo=True, future=True)

#ngine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

async def create_all_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
