from sqlalchemy.orm import Session

from todo.dto import role
from todo.models.models import Role


def create_role(data: role.Role, db: Session):
    role = Role(title=data.title)
    try:
        db.add(role)
        db.commit()
        db.refresh(role)
    except Exception as e:
        print(e)
    return role


def get_role(id: int, db: Session):
    return db.query(Role).filter(Role.id == id).first()


def update(data: role.Role, db: Session, id: int):
    dashboard_up = db.query(Role).filter(Role.id == id).first()
    dashboard_up.title = data.title
    db.add(dashboard_up)
    db.commit()
    db.refresh(dashboard_up)
    return dashboard_up


def remove(db: Session, id: int):
    dashboard = db.query(Role).filter(Role.id == id).delete()
    db.commit()
    return dashboard


def get_all(db: Session):
    return db.query(Role).all()
