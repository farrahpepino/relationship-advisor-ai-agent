from pydantic import BaseModel
from datetime import datetime

class Chat_Out(BaseModel):
    id: str
    user_id: str
    title: str
    last_opened: datetime

    model_config = {"from_attributes": True}