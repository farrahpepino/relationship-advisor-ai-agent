from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.services.auth_service import Auth_Service


auth_service = Auth_Service()

class Auth:
    def get_user(
        token: str,
        db: Session = Depends(get_db)
    ):
        return auth_service.authenticate_account(db, token)