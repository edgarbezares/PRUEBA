from fastapi import FastAPI
from routes.user import user
import uvicorn


app=FastAPI()

app.include_router(user)