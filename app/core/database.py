from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from app.core.config import settings

# 1. Создаем асинхронный движок для работы с БД
engine = create_async_engine(settings.DATABASE_URL_asyncpg, echo=True)

# 2. Создаем фабрику сессий (через неё мы будем делать запросы к БД)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# 3. Базовый класс для всех наших будущих моделей/таблиц
class Base(DeclarativeBase):
    pass

# Зависимость (Dependency) для получения сессии БД в FastAPI
async def get_async_session():
    async with async_session_maker() as session:
        yield session