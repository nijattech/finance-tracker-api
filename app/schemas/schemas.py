from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from app.models.all_models import TransactionType


# ==========================================
# СХЕМЫ КАТЕГОРИЙ (Category)
# ==========================================

class CategoryCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="Название категории")
    type: TransactionType = Field(..., description="Тип: income или expense")
    monthly_limit: float | None = Field(None, ge=0, description="Месячный лимит (необязательно)")


class CategoryResponse(CategoryCreate):
    id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)


# ==========================================
# СХЕМЫ ТРАНЗАКЦИЙ (Transaction)
# ==========================================

class TransactionCreate(BaseModel):
    category_id: int = Field(..., description="ID категории")
    amount: float = Field(..., gt=0, description="Сумма (должна быть больше 0)")
    description: str | None = Field(None, max_length=255, description="Описание (необязательно)")


class TransactionResponse(TransactionCreate):
    id: int
    user_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# ==========================================
# СХЕМЫ ПОЛЬЗОВАТЕЛЕЙ И АВТОРИЗАЦИИ
# ==========================================

class UserCreate(BaseModel):
    email: str
    password: str = Field(..., min_length=6, description="Пароль не менее 6 символов")


class UserResponse(BaseModel):
    id: int
    email: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"