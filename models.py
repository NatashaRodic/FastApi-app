from pydantic import BaseModel
from typing import Optional

class ToDoItem(BaseModel):
    id: int
    title: str
    description: Optional[str] = None