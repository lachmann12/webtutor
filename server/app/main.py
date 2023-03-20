from fastapi import FastAPI
from fastapi import HTTPException

from .models import User
from .database import database
from . import crud as users


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

    # Return the user as a response
    return user

@app.get("/tutor/{user_id}")
async def get_user(user_id: int):
    # Look up the user by ID in the database
    user_data = {"id": user_id, "name": "John Doe", "email": "john.doe@example.com"}
    user = User(**user_data)

    # Return the user as a response
    return user