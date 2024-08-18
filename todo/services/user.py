from sqlalchemy.orm import Session

from todo.dto import user
from todo.models.models import User
from todo.services.role import get_role


def create_user(data: user.User, db: Session):
    role = get_role(data.role_id, db)
    user = User(name=data.name, email=data.email, password=data.password, role=role, role_id=data.role_id)
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        print(e)
    return user


def get_user(id: int, db: Session):
    return db.query(User).filter(User.id == id).first()


def update(data: user.User, db: Session, id: int):
    user_up = db.query(User).filter(User.id == id).first()
    user_up.name = data.name
    user_up.email = data.email
    user_up.password = data.password
    user_up.role = get_role(data.role_id, db)
    user_up.role_id = data.role_id
    db.add(user_up)
    db.commit()
    db.refresh(user_up)
    return user_up


def remove(db: Session, id: int):
    user = db.query(User).filter(User.id == id).delete()
    db.commit()
    return user


def get_all(db: Session):
    return db.query(User).all()
