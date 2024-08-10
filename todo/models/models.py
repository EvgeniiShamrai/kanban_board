from typing import List

from sqlalchemy import ForeignKey, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.sql import func

from db.database import Base


class Dashboard(Base):
    __tablename__ = 'dashboard'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(225), index=True)
    tasks: Mapped[List["Task"]] = relationship(back_populates="dashboard")


class Status(Base):
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(225), index=True)
    tasks: Mapped[List["Task"]] = relationship(back_populates="status")


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(225), index=True)
    description = Column(String(), index=True)
    status = relationship(Status, back_populates='tasks')
    status_id = Column(Integer, ForeignKey('status.id'))
    dashboard = relationship(Dashboard, back_populates='tasks')
    dashboard_id = Column(Integer, ForeignKey('dashboard.id'))
    comments: Mapped[List["Comment"]] = relationship(back_populates="task")
    children: Mapped[List["Subtask"]] = relationship()
    create_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class Subtask(Base):
    __tablename__ = "subtask"
    parent: Mapped[int] = Column(ForeignKey("task.id"), primary_key=True)
    children: Mapped[int] = Column(
        ForeignKey("task.id"), primary_key=True
    )
    child: Mapped["Task"] = relationship()


class Comment(Base):
    """Надо сделать добавление файлов и картинок к комментарию"""
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(225), index=True)
    description = Column(String(), index=True)
    author = Column(String(150), index=True, default=False)
    task = relationship(Task, back_populates='comments')
    task_id = Column(Integer, ForeignKey('task.id'))
    create_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
