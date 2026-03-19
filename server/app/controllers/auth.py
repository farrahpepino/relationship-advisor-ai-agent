from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services.auth_service import Auth_Service
from app.dtos.user import User_Dto
from app.dtos.token import Token_Request
from app.database.session import get_db

router = APIRouter()
auth_service = Auth_Service()

@router.post("/auth/google", response_model=User_Dto)
def google_auth(body: Token_Request, db: Session = Depends(get_db)):
    return auth_service.authenticate_account(db, body.token)