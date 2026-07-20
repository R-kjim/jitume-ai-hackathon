from server.app.config.config import variables
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

DATABASE_URL= variables.database_url
ASYNC_DATABASE_URL= variables.async_database_url
engine=create_engine(url=DATABASE_URL)
async_engine= create_async_engine(
    url=ASYNC_DATABASE_URL, 
    echo=False,
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
    pool_recycle=1800
)

""" Production environment engine setup """
# engine = create_engine(
#     url=variables.database_url,
#     pool_size=10,
#     max_overflow=20,
#     pool_timeout=30,
#     pool_recycle=1800
# )

SessionLocal=sessionmaker(bind=engine, autoflush=True, autocommit=False)

AsyncSessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)

def get_db():
    db=SessionLocal()
    try:
        yield db
        db.flush()
    finally:
        db.close()

async def get_async_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.flush()
        finally:
            await session.close()