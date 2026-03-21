from sqlalchemy import Column, ForeignKey, String, TIMESTAMP, func
from app.database.base import Base

class Message(Base):
    __tablename__ = "messages"
    
    id = Column(String(255), primary_key=True, unique=True)
    conversation_id = Column(String(255), ForeignKey("conversations.id"), nullable=False)
    content = Column(String(1000), nullable=False)
    role = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP)