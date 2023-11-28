import datetime

from pydantic import BaseModel, validator
from domain.user.user_schema import User

class Todo(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    user: User | None
    modify_date: datetime.datetime | None = None

    class Config:
        orm_mode = True

class TodoCreate(BaseModel):
    subject: str
    content: str

    @validator('subject', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v


class TodoList(BaseModel):
    total: int = 0
    todo_list: list[Todo] = []


class TodoUpdate(TodoCreate):
    todo_id: int


class TodoDelete(BaseModel):
    todo_id: int