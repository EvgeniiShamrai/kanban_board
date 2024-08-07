import datetime

from pydantic import BaseModel


class Task(BaseModel):
    title: str
    description: str
    status_id: int
    dashboard_id: int
    create_at: datetime.datetime
    updated_at: datetime.datetime
