from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserPartialUpdate, UserResponse, UserUpdate

router = APIRouter()


@router.post("", response_model=UserResponse, status_code=201)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("", response_model=list[UserResponse])
async def get_all_users(db: Session = Depends(get_db)):
    users = db.execute(select(User)).scalars().all()
    return users


@router.get("/{id}", response_model=UserResponse)
async def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = db.execute(select(User).filter(User.id == id)).scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{id}", response_model=UserResponse)
async def update_user(id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    user = db.execute(select(User).filter(User.id == id)).scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user_update.dict().items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user


@router.patch("/{id}", response_model=UserResponse)
async def partially_update_user(
    id: int, user_update: UserPartialUpdate, db: Session = Depends(get_db)
):
    user = db.execute(select(User).filter(User.id == id)).scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user


@router.delete("/{id}", status_code=204)
async def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.execute(select(User).filter(User.id == id)).scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return None
