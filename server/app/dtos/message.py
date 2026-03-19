from pydantic import BaseModel

class Message_Request(BaseModel):
    input: str