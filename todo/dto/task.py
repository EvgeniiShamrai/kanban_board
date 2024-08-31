import datetime

from pydantic import BaseModel


class Task(BaseModel):
    title: str
    description: str
    complexity: float
    status_id: int
    dashboard_id: int
    executor_id: int
    author_id: int
    parent_id: int | None
    create_at: datetime.datetime
    updated_at: datetime.datetime
