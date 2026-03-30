from fastapi import FastAPI
from app.routes import router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Trade Opportunities API is running 🚀"}

app.include_router(router)