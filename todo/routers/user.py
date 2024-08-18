from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from todo.dto import user as UserDto
from todo.services import user as UserService

router = APIRouter()


@router.post('/', tags=['user'])
async def create(data: UserDto.User = None, db: Session = Depends(get_db)):
    return UserService.create_user(data, db)


@router.get('/{id}', tags=['user'])
async def get(id: int = None, db: Session = Depends(get_db)):
    return UserService.get_user(id, db)


@router.get('/', tags=['user'])
async def get_all(db: Session = Depends(get_db)):
    return UserService.get_all(db)


@router.put('/{id}', tags=['user'])
async def update(id: int = None, data: UserDto.User = None, db: Session = Depends(get_db)):
    return UserService.update(data, db, id)


@router.delete('/{id}', tags=['user'])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return UserService.remove(db, id)
