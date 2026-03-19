from sqlalchemy import Column, String, ForeignKey, TIMESTAMP, func
from app.database.base import Base

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(String(255), primary_key=True, unique=True)
    user_id = Column(String(255), ForeignKey("users.id"), nullable=False,)
    title = Column(String(255), nullable=False)
    last_opened = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())