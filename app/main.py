from fastapi import FastAPI
from app.routes import users

app = FastAPI(title="AI Study Planner API")

app.include_router(users.router)

@app.get("/")
def home():
    return {"message": "AI Study Planner API is running 🚀"}
