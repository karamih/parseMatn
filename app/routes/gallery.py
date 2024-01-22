from typing import List
from fastapi import Depends, status, APIRouter

from sqlalchemy.orm import Session

from app import models, schemas
from app.oauth2 import get_current_user
from app.database import get_db



router = APIRouter(prefix="/users", tags=["gallery"])


@router.post("/gallery", status_code=status.HTTP_200_OK, response_model=List[schemas.GalleryContent])
def profile(current_user: int = Depends(get_current_user), db: Session = Depends(get_db)):    
    contents = db.query(models.Image).filter(models.Image.user_id == list(dict(current_user).values())[0]).all()    
    return contents
