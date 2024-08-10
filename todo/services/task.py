from sqlalchemy.orm import Session

from todo.dto import task
from todo.models.models import Task
from todo.services.dashboard import get_dashboard
from todo.services.status import get_status


def create_task(data: task.Task, db: Session):
    status = get_status(data.status_id, db)
    dashboard = get_dashboard(data.dashboard_id, db)
    task = Task(title=data.title, description=data.description, status_id=data.status_id, status=status,
                dashboard=dashboard, dashboard_id=data.dashboard_id)
    try:
        db.add(task)
        db.commit()
        db.refresh(task)
    except Exception as e:
        print(e)
    return task


def get_task(id: int, db: Session):
    return db.query(Task).filter(Task.id == id).first()


def get_comments(id: int, db: Session):
    task = get_task(id, db)
    return task.comments


def get_subtask(id: int, db: Session):
    task = get_task(id, db)
    return task.children


def update(data: task.Task, db: Session, id: int):
    task_up = db.query(Task).filter(Task.id == id).first()
    task_up.title = data.title
    task_up.description = data.description
    task_up.status_id = data.status.id
    db.add(task_up)
    db.commit()
    db.refresh(task_up)
    return task_up


def remove(db: Session, id: int):
    task = db.query(Task).filter(Task.id == id).delete()
    db.commit()
    return task


def get_all(db: Session):
    return db.query(Task).all()
