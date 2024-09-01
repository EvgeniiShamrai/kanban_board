from sqlalchemy.orm import Session

from todo.dto import task
from todo.models.models import Task
from todo.services.dashboard import get_dashboard
from todo.services.status import get_status
from todo.services.user import get_user_by_id


def create_task(data: task.Task, db: Session):
    status = get_status(data.status_id, db)
    executor = get_user_by_id(data.executor_id, db)
    author = get_user_by_id(data.author_id, db)
    dashboard = get_dashboard(data.dashboard_id, db)
    if data.parent_id is None:
        parent = None
    else:
        parent = get_task(data.parent_id, db)
    task = Task(title=data.title, description=data.description, labor_intensity=data.labor_intensity,
                start_task=data.start_task, dead_line_task=data.dead_line_task, status_id=data.status_id,
                status=status,
                dashboard=dashboard, dashboard_id=data.dashboard_id, executor=executor, executor_id=data.executor_id,
                author=author, author_id=data.author_id, parent=parent, parent_id=data.parent_id)
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
    return task.tasks


def update(data: task.Task, db: Session, id: int):
    task_up = db.query(Task).filter(Task.id == id).first()
    task_up.title = data.title
    task_up.description = data.description
    task_up.labor_intensity = data.labor_intensity
    task_up.status = get_status(data.status_id, db)
    task_up.start_task = data.start_task
    task_up.dead_line_task = data.dead_line_task
    task_up.executor = get_user_by_id(data.executor_id, db)
    task_up.author = get_user_by_id(data.author_id, db)
    task_up.executor_id = data.executor_id
    task_up.author_id = data.author_id
    task_up.status_id = data.status_id
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
