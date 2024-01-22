import base64
import pathlib

from fastapi import Depends, status, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.image_generator.translation import translation_chain
from app.oauth2 import get_current_user
from app import models, schemas
from app.image_generator.text_to_image import query
from app.database import get_db



router = APIRouter(prefix="/generate", tags=["Image Generation"])
UPLOAD_DIR = pathlib.Path(__file__).parent.parent / "generated_images"


@router.post("/", status_code=status.HTTP_201_CREATED)
def generate(user_input: schemas.Command, current_user: int = Depends(get_current_user), db: Session = Depends(get_db)):    
    try:
        user_command = translation_chain.run(user_input.command)

        image_bytes = query({
            "inputs": user_command,
        })
        
        img_recovered = base64.b64encode(image_bytes).decode('utf-8')
                
        image_arguments = {
            "user_id" : list(dict(current_user).values())[0],
            "image_prompt" : user_command,
            "image" : img_recovered
        }
        
        new_image = models.Image(**image_arguments)
        print(new_image)
        db.add(new_image)
        db.commit()

        return img_recovered

    except:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail='not work')
