from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    user: str

@app.get("/auth/me")
async def auth_me(user: User):
    return {"user": user.user, "ping": "pong"}