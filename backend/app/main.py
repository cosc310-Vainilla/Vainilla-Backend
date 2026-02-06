from fastapi import FastAPI
from app.routers.items_routers import router as items_router

app = FastAPI()

app.include_router(items_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Food Delivery API"}
