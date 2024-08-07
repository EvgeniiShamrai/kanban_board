from sqlalchemy.orm import Session

from todo.dto import status
from todo.models.models import Status


def create_status(data: status.Status, db: Session):
    obj = Status(title=data.title)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def get_status(id: int, db: Session) -> Status:
    return db.query(Status).filter(Status.id == id).first()


def update(data: status.Status, db: Session, id: int):
    task_up = db.query(Status).filter(Status.id == id).first()
    task_up.title = data.title
    db.add(task_up)
    db.commit()
    db.refresh(task_up)
    return task_up


def remove(db: Session, id: int):
    task = db.query(Status).filter(Status.id == id).delete()
    db.commit()
    return task


def get_all(db: Session):
    return db.query(Status).all()
