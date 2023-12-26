import base64
import pathlib
import uuid
import io
from PIL import Image
from fastapi import Depends, status, APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.image_generator.translation import translation_chain
from app.oauth2 import get_current_user
from app import schemas
from app.image_generator.text_to_image import query

router = APIRouter(prefix="/generate", tags=["Image Generation"])
UPLOAD_DIR = pathlib.Path(__file__).parent.parent / "generated_images"


@router.post("/", status_code=status.HTTP_201_CREATED)
def generate(user_input: schemas.Command, current_user: int = Depends(get_current_user)):
    try:
        user_command = translation_chain.run(user_input.command)
        print(user_command)

        image_bytes = query({
            "inputs": user_command,
        })
        # print('generation works')

        img_recovered = base64.b64encode(image_bytes)
        image = Image.open(io.BytesIO(image_bytes))
        full_path = UPLOAD_DIR / f"{uuid.uuid4()}.jpg"
        image.save(full_path)
         
        # print(img_recovered)
        return img_recovered

    except:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail='not work')
