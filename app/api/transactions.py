from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_async_session
from app.schemas.schemas import TransactionCreate, TransactionResponse
from app.core import crud
from app.models.all_models import User
from app.api.deps import get_current_user

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.post("/", response_model=TransactionResponse, status_code=status.HTTP_201_CREATED)
async def create_new_transaction(
    transaction_data: TransactionCreate,
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(get_current_user)
):
    """Create a new transaction for the authenticated user"""
    return await crud.create_transaction(db, transaction_data, user_id=current_user.id)


@router.get("/", response_model=list[TransactionResponse])
async def get_transactions(
    transaction_type: str | None = Query(None, description="Filter by transaction type: income or expense"),
    category_id: int | None = Query(None, description="Filter by category ID"),
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(get_current_user)
):
    """Retrieve filtered transactions for the authenticated user"""
    return await crud.get_filtered_transactions(
        db, user_id=current_user.id, transaction_type=transaction_type, category_id=category_id
    )