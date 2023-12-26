from fastapi import FastAPI
from app.routes import users, imageGen
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return {"message": "Hello"}


app.include_router(router=users.router)
app.include_router(router=imageGen.router)
