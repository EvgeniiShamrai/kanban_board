from pydantic import BaseModel


class Role(BaseModel):
    title: str
