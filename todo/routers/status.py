from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from todo.dto import status as StatusDto
from todo.services import status as StatusService

router = APIRouter()


@router.post('/', tags=['status'])
async def create(data: StatusDto.Status = None, db: Session = Depends(get_db)):
    return StatusService.create_status(data, db)


@router.get('/{id}', tags=['status'])
async def get(id: int = None, db: Session = Depends(get_db)):
    return StatusService.get_status(id, db)


@router.get('/', tags=['status'])
async def get_all(db: Session = Depends(get_db)):
    return StatusService.get_all(db)


@router.put('/{id}', tags=['status'])
async def update(id: int = None, data: StatusDto.Status = None, db: Session = Depends(get_db)):
    return StatusService.update(data, db, id)


@router.delete('/{id}', tags=['status'])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return StatusService.remove(db, id)
