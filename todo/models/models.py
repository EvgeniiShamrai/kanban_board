from typing import List

from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.sql import func

from db.database import Base


class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(30), default=False, index=True)
    users: Mapped[List["User"]] = relationship(back_populates="role")


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


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), default=False, index=True)
    email = Column(String(50), default=False, index=True)
    password = Column(String(30), default=False, index=True)
    role = relationship(Role, back_populates='users')
    role_id = Column(Integer, ForeignKey("role.id"))
    tasks: Mapped[List["Task"]] = relationship("Task", back_populates="executor", foreign_keys="[Task.executor_id]")
    created_tasks: Mapped[List["Task"]] = relationship("Task", back_populates="author", foreign_keys="[Task.author_id]")
    comments: Mapped[List["Comment"]] = relationship(back_populates="author")
    create_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(225), index=True)
    description = Column(String(), index=True)
    complexity = Column(Float, index=True)
    status = relationship(Status, back_populates='tasks')
    status_id = Column(Integer, ForeignKey('status.id'))
    dashboard = relationship(Dashboard, back_populates='tasks')
    dashboard_id = Column(Integer, ForeignKey('dashboard.id'))
    comments: Mapped[List["Comment"]] = relationship(back_populates="task")
    parent_id = Column(Integer, ForeignKey('task.id'))
    parent = relationship('Task', remote_side=[id])
    tasks: Mapped[List["Task"]] = relationship(back_populates="parent")
    executor_id = Column(Integer, ForeignKey('user.id'))
    author_id = Column(Integer, ForeignKey('user.id'))
    executor = relationship("User", back_populates='tasks', foreign_keys=[executor_id])
    author = relationship("User", back_populates='created_tasks', foreign_keys=[author_id])

    create_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class Comment(Base):
    """Надо сделать добавление файлов и картинок к комментарию"""
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(225), index=True)
    description = Column(String(), index=True)
    task = relationship(Task, back_populates='comments')
    task_id = Column(Integer, ForeignKey('task.id'))
    author = relationship(User, back_populates='comments')
    author_id = Column(Integer, ForeignKey('user.id'))
    create_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
