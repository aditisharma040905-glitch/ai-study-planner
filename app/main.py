from fastapi import FastAPI
from app.routes import users
from app.database import Base, engine
from app import models

app = FastAPI(title="AI Study Planner API")

Base.metadata.create_all(bind=engine)

app.include_router(users.router)

@app.get("/")
def home():
    return {"message": "AI Study Planner API is running 🚀"}
