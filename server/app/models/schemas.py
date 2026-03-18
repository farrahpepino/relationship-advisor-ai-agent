from pydantic import BaseModel
from typing import List
from datetime import datetime


class MessageSchema(BaseModel):
    role: str
    content: str
    conversation_id: str
    created_at: datetime
        
class CoversationSchema(BaseModel):
    user_id: str
    messages: List[MessageSchema] = []