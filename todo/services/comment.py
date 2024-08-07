from sqlalchemy.orm import Session

from todo.dto import comment
from todo.models.models import Comment
from todo.services.task import get_task


def create_comment(data: comment.Comment, db: Session):
    task = get_task(data.task_id, db)
    comment = Comment(title=data.title, description=data.description, author=data.author, task=task,
                      task_id=data.task_id)
    try:
        db.add(comment)
        db.commit()
        db.refresh(comment)
    except Exception as e:
        print(e)
    return comment


def get_comment(id: int, db: Session):
    return db.query(Comment).filter(Comment.id == id).first()


def update(data: comment.Comment, db: Session, id: int):
    comment_up = db.query(Comment).filter(Comment.id == id).first()
    comment_up.title = data.title
    comment_up.description = data.description
    comment_up.author = data.author
    db.add(comment_up)
    db.commit()
    db.refresh(comment_up)
    return comment_up


def remove(db: Session, id: int):
    comment = db.query(Comment).filter(Comment.id == id).delete()
    db.commit()
    return comment


def get_all(db: Session):
    return db.query(Comment).all()
