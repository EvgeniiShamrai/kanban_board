from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from todo.dto import task as TaskDto
from todo.services import task as TaskService

router = APIRouter()


@router.post('/', tags=['task'])
async def create(data: TaskDto.Task = None, db: Session = Depends(get_db)):
    return TaskService.create_task(data, db)


@router.get('/{id}', tags=['task'])
async def get(id: int = None, db: Session = Depends(get_db)):
    return TaskService.get_task(id, db)


@router.get('/', tags=['task'])
async def get_all(db: Session = Depends(get_db)):
    return TaskService.get_all(db)


@router.get('/{id}/comments', tags=['task'])
async def get_comments(id: int = None, db: Session = Depends(get_db)):
    return TaskService.get_comments(id, db)


@router.get('/{id}/subtaska', tags=['task'])
async def get_comments(id: int = None, db: Session = Depends(get_db)):
    return TaskService.get_subtask(id, db)


@router.put('/{id}', tags=['task'])
async def update(id: int = None, data: TaskDto.Task = None, db: Session = Depends(get_db)):
    return TaskService.update(data, db, id)


@router.delete('/{id}', tags=['task'])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return TaskService.remove(db, id)
