from sqlalchemy.orm import Session

from todo.dto import comment
from todo.models.models import Comment
from todo.services.task import get_task
from todo.services.user import get_user


def create_comment(data: comment.Comment, db: Session):
    task = get_task(data.task_id, db)
    author = get_user(data.author_id, db)
    comment = Comment(title=data.title, description=data.description, author=author, author_id=data.author_id,
                      task=task,
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
    comment_up.author = get_user(data.author_id, db)
    comment_up.author_id = data.author_id
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
