import pathlib
import uuid
import io
from PIL import Image
from fastapi import Depends, status, APIRouter
from fastapi.responses import FileResponse
from app.image_generator.translation import translation_chain
from app.oauth2 import get_current_user
from app import schemas
from app.image_generator.text_to_image import query

router = APIRouter(prefix="/generate", tags=["Image Generation"])
UPLOAD_DIR = pathlib.Path(__file__).parent.parent / "generated_images"


@router.get("/", status_code=status.HTTP_201_CREATED)
def generate(command: schemas.Command, current_user: int = Depends(get_current_user)):
    try:
        user_command = translation_chain.run(command.command)
        print(user_command)
    except:
        return {"error": "openai api key error"}

    image_bytes = query({
        "inputs": user_command,
    })

    image = Image.open(io.BytesIO(image_bytes))

    full_path = UPLOAD_DIR / f"{uuid.uuid4()}.jpg"
    image.save(full_path)

    return {"message": "Done"}
