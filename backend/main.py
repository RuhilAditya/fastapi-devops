from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from typing import List

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB Connection
# 'mongodb' is the name of the service we will define in Docker
client = AsyncIOMotorClient("mongodb://mongodb:27017")
db = client.devops_db
collection = db.services

class Service(BaseModel):
    name: str
    status: str

@app.get("/")
def health_check():
    return {"status": "Systems Operational", "database": "Connected"}

@app.get("/services", response_model=List[Service])
async def get_services():
    services = await collection.find().to_list(1000)
    return services

@app.post("/services")
async def add_service(service: Service):
    await collection.insert_one(service.dict())
    return {"message": "Saved to MongoDB"}