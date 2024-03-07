from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from simplecrud.database import get_db
from simplecrud.crud import user_crud
from simplecrud.schemas.user import UserCreate, UserRead, UserUpdate 

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserRead)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    return user_crud.create_user(db, user_data.dict())


@router.get("/{user_id}", response_model=UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = user_crud.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=UserRead)
def update_user(
    user_id: int, updated_user_data: UserUpdate, db: Session = Depends(get_db)
):
    user = user_crud.update_user(
        db, user_id, updated_user_data.dict(exclude_unset=True)
    )
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
