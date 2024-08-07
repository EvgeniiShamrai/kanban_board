from sqlalchemy.orm import Session

from todo.dto import dashboard
from todo.models.models import Dashboard


def create_dashboard(data: dashboard.Dashboard, db: Session):
    dashboard = Dashboard(title=data.title)
    try:
        db.add(dashboard)
        db.commit()
        db.refresh(dashboard)
    except Exception as e:
        print(e)
    return dashboard


def get_dashboard(id: int, db: Session):
    return db.query(Dashboard).filter(Dashboard.id == id).first()


def update(data: dashboard.Dashboard, db: Session, id: int):
    dashboard_up = db.query(Dashboard).filter(Dashboard.id == id).first()
    dashboard_up.title = data.title
    db.add(dashboard_up)
    db.commit()
    db.refresh(dashboard_up)
    return dashboard_up


def remove(db: Session, id: int):
    dashboard = db.query(Dashboard).filter(Dashboard.id == id).delete()
    db.commit()
    return dashboard


def get_all(db: Session):
    return db.query(Dashboard).all()
