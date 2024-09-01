import datetime

from pydantic import BaseModel, PositiveFloat


class Task(BaseModel):
    title: str
    description: str
    labor_intensity: PositiveFloat
    status_id: int
    dashboard_id: int
    executor_id: int
    author_id: int
    parent_id: int | None
    start_task: datetime.datetime
    dead_line_task: datetime.datetime
    create_at: datetime.datetime
    updated_at: datetime.datetime
