from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "From FastAPI"}


@app.post("/auth/me")
async def auth_me(username: str):
    return {"user": username, "ping": "pong"}
