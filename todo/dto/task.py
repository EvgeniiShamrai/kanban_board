import datetime

from pydantic import BaseModel
from typing import Optional


class Task(BaseModel):
    title: str
    description: str
    status_id: int
    dashboard_id: int
    create_at: datetime.datetime
    updated_at: datetime.datetime
