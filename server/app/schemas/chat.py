from pydantic import BaseModel
from typing import Optional, Text
from uuid import UUID


class UserQuery(BaseModel):
    message: Text
    session_id: str

class  N8nResponse(BaseModel):
    status: str
    coverage: Optional[float]
    message: str