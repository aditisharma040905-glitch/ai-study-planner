from fastapi import FastAPI
from app.routes import users, notes
from app.database import Base, engine

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Study Planner API")

app.include_router(users.router)
app.include_router(notes.router)


@app.get("/")
def root():
    return {"message": "AI Study Planner API is running 🚀"}
