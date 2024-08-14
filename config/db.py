from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData

engine = create_async_engine('postgresql+asyncpg://root:root%40123@localhost:5432/singlish_to_sinhala', echo=True)

meta = MetaData()

async_session = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(meta.create_all)
