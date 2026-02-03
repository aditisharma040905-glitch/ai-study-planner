from fastapi import FastAPI
from app.routes import users, notes
from app.database import Base, engine
from app.routes import task
from app.routes import ai





# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Study Planner API")

app.include_router(users.router)
app.include_router(notes.router)

app.include_router(task.router)
app.include_router(ai.router)


@app.get("/")
def root():
    return {"message": "AI Study Planner API is running 🚀"}
