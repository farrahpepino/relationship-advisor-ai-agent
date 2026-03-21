from pydantic import BaseModel
from datetime import datetime

class Message_Out(BaseModel):
    id: str
    conversation_id: str
    content: str
    role: str
    created_at: datetime

    model_config = {"from_attributes": True}