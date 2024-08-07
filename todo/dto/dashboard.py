from pydantic import BaseModel


class Dashboard(BaseModel):
    title: str
