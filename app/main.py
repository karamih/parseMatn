from fastapi import FastAPI
from app.routes import users, imageGen


app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello"}


app.include_router(router=users.router)
app.include_router(router=imageGen.router)
