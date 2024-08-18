import datetime

from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    password: str
    role_id: int
    create_at: datetime.datetime
    updated_at: datetime.datetime
