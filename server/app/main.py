from fastapi import FastAPI
from fastapi import HTTPException

from .models import User
from .api_models import TutorQuery, ChatCompletion
from .database import database
from . import crud as users
from . import chatgpt

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    # Look up the user by ID in the database
    user_data = {"id": user_id, "name": "John Doe", "email": "john.doe@example.com"}
    user = User(**user_data)
    return user

@app.post("/tutor")
async def get_response(data: TutorQuery):
    print(data)
    chat = chatgpt.generate_gpt(data.input)
    return ChatCompletion(**chat)