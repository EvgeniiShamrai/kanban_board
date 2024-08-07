from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from todo.dto import comment as CommentDto
from todo.services import comment as CommentService

router = APIRouter()


@router.post('/', tags=['comment'])
async def create(data: CommentDto.Comment = None, db: Session = Depends(get_db)):
    return CommentService.create_comment(data, db)


@router.get('/{id}', tags=['comment'])
async def get(id: int = None, db: Session = Depends(get_db)):
    return CommentService.get_comment(id, db)


@router.get('/', tags=['comment'])
async def get_all(db: Session = Depends(get_db)):
    return CommentService.get_all(db)


@router.put('/{id}', tags=['comment'])
async def update(id: int = None, data: CommentDto.Comment = None, db: Session = Depends(get_db)):
    return CommentService.update(data, db, id)


@router.delete('/{id}', tags=['comment'])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return CommentService.remove(db, id)
