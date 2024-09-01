import datetime
import json
from typing import Self

from pydantic import BaseModel, PositiveFloat, ValidationError, ValidationInfo, field_validator, model_validator
from fastapi import HTTPException, status


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

    @model_validator(mode='after')
    def check_passwords_match(self) -> Self:
        start = self.start_task
        dead = self.dead_line_task
        labor_intensity = self.labor_intensity
        if labor_intensity <= 0:
            raise ValueError('Input should be greater than 0')
        if start is not None and dead is not None and start >= dead:
            raise ValueError('Start time can not be bigger then deadline')
        return self