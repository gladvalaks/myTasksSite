import pydantic


class TaskPriority(pydantic.BaseModel):
    id: int
    title: str
    order: int
