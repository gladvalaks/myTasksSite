import pydantic

class Task_priority(pydantic.BaseModel):
    id: int
    title: str
    order: int