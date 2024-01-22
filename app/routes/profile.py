from fastapi import Depends, status, APIRouter
from sqlalchemy.orm import Session

from app.oauth2 import get_current_user
from app import models, schemas
from app.database import get_db



router = APIRouter(prefix="/users", tags=["Profile"])


@router.post("/profile", status_code=status.HTTP_200_OK, response_model=schemas.UserProfile)
def profile(current_user: int = Depends(get_current_user), db: Session = Depends(get_db)):    
    user = db.query(models.User).filter(models.User.id == list(dict(current_user).values())[0]).first()
    return user
