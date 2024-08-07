import datetime

from pydantic import BaseModel


class Comment(BaseModel):
    title: str
    description: str
    author: str
    task_id: int
    create_at: datetime.datetime
    updated_at: datetime.datetime
