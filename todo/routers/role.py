from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from todo.dto import role as RoleDto
from todo.services import role as RoleService

router = APIRouter()


@router.post('/', tags=['role'])
async def create(data: RoleDto.Role = None, db: Session = Depends(get_db)):
    return RoleService.create_role(data, db)


@router.get('/{id}', tags=['role'])
async def get(id: int = None, db: Session = Depends(get_db)):
    return RoleService.get_role(id, db)


@router.get('/', tags=['role'])
async def get_all(db: Session = Depends(get_db)):
    return RoleService.get_all(db)


@router.put('/{id}', tags=['role'])
async def update(id: int = None, data: RoleDto.Role = None, db: Session = Depends(get_db)):
    return RoleService.update(data, db, id)


@router.delete('/{id}', tags=['role'])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return RoleService.remove(db, id)
