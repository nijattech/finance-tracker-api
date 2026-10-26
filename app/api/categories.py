from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_async_session
from app.schemas.schemas import CategoryCreate, CategoryResponse
from app.core import crud
from app.models.all_models import User
from app.api.deps import get_current_user

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
async def create_new_category(
    category_data: CategoryCreate,
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(get_current_user)
):
    """Create a new category for the authenticated user"""
    return await crud.create_category(db, category_data, user_id=current_user.id)


@router.get("/", response_model=list[CategoryResponse])
async def get_categories(
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(get_current_user)
):
    """Retrieve all categories for the authenticated user"""
    return await crud.get_user_categories(db, user_id=current_user.id)