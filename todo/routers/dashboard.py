from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from todo.dto import dashboard as DashboardDto
from todo.services import dashboard as DashboardService

router = APIRouter()


@router.post('/', tags=['dashboard'])
async def create(data: DashboardDto.Dashboard = None, db: Session = Depends(get_db)):
    return DashboardService.create_dashboard(data, db)


@router.get('/{id}', tags=['dashboard'])
async def get(id: int = None, db: Session = Depends(get_db)):
    return DashboardService.get_dashboard(id, db)


@router.get('/', tags=['dashboard'])
async def get_all(db: Session = Depends(get_db)):
    return DashboardService.get_all(db)


@router.put('/{id}', tags=['dashboard'])
async def update(id: int = None, data: DashboardDto.Dashboard = None, db: Session = Depends(get_db)):
    return DashboardService.update(data, db, id)


@router.delete('/{id}', tags=['dashboard'])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return DashboardService.remove(db, id)
