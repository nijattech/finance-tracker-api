from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_async_session
from app.core import crud
from app.models.all_models import User
from app.api.deps import get_current_user

router = APIRouter(prefix="/stats", tags=["Analytics & Statistics"])


@router.get("/summary")
async def get_financial_summary(
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(get_current_user)
):
    """Get financial summary including total income, expenses, and current balance"""
    return await crud.get_user_stats(db, user_id=current_user.id)