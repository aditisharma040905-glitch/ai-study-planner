from fastapi import FastAPI

app = FastAPI(title="AI Study Planner")

@app.get("/")
def home():
    return {"message": "AI Study Planner API is running 🚀"}
