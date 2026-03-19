from fastapi import FastAPI

from app.controllers import auth, chat
from app.database.base import Base
from app.database.session import engine

from app.models import user

app = FastAPI()

app.include_router(auth.router)
app.include_router(chat.router)


Base.metadata.create_all(bind=engine)