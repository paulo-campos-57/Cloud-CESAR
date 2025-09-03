from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.post("/auth/me")
async def auth_me(username: str):
    return {"user": username, "ping": "pong"}