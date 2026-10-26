from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.all_models import User, Category, Transaction
from app.schemas.schemas import UserCreate, CategoryCreate, TransactionCreate
from app.core.security import hash_password


# --- РАБОТА С ПОЛЬЗОВАТЕЛЯМИ ---

async def get_user_by_email(db: AsyncSession, email: str) -> User | None:
    result = await db.execute(select(User).where(User.email == email))
    return result.scalars().first()


async def get_user_by_id(db: AsyncSession, user_id: int) -> User | None:
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalars().first()


async def create_user(db: AsyncSession, user_data: UserCreate) -> User:
    hashed_pwd = hash_password(user_data.password)
    db_user = User(email=user_data.email, hashed_password=hashed_pwd)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


# --- РАБОТА С КАТЕГОРИЯМИ ---

async def create_category(db: AsyncSession, category_data: CategoryCreate, user_id: int) -> Category:
    db_category = Category(**category_data.model_dump(), user_id=user_id)
    db.add(db_category)
    await db.commit()
    await db.refresh(db_category)
    return db_category


async def get_user_categories(db: AsyncSession, user_id: int) -> list[Category]:
    result = await db.execute(select(Category).where(Category.user_id == user_id))
    return list(result.scalars().all())


# --- РАБОТА С ТРАНЗАКЦИЯМИ И АНАЛИТИКОЙ ---

async def create_transaction(db: AsyncSession, transaction_data: TransactionCreate, user_id: int) -> Transaction:
    db_transaction = Transaction(**transaction_data.model_dump(), user_id=user_id)
    db.add(db_transaction)
    await db.commit()
    await db.refresh(db_transaction)
    return db_transaction


async def get_user_transactions(db: AsyncSession, user_id: int) -> list[Transaction]:
    result = await db.execute(select(Transaction).where(Transaction.user_id == user_id))
    return list(result.scalars().all())


# 1. Получение транзакций с фильтрацией (Глава 4)
# 1. Получение транзакций с фильтрацией (Глава 4)
async def get_filtered_transactions(
        db: AsyncSession,
        user_id: int,
        transaction_type: str | None = None,
        category_id: int | None = None
) -> list[Transaction]:
    query = select(Transaction).where(Transaction.user_id == user_id)

    if transaction_type:
        query = query.where(Transaction.type == transaction_type)
    if category_id:
        query = query.where(Transaction.category_id == category_id)

    result = await db.execute(query)
    return list(result.scalars().all())


# 2. Расчет общей статистики (Глава 4 - Исправлено под SQLite)
async def get_user_stats(db: AsyncSession, user_id: int) -> dict:
    # Запрашиваем все транзакции пользователя
    result = await db.execute(select(Transaction).where(Transaction.user_id == user_id))
    transactions = result.scalars().all()

    total_income = sum(t.amount for t in transactions if t.type == "income")
    total_expense = sum(t.amount for t in transactions if t.type == "expense")

    return {
        "total_income": float(total_income),
        "total_expense": float(total_expense),
        "balance": float(total_income - total_expense)
    }