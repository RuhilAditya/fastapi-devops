from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Service(BaseModel):
    name: str
    status: str

# Our "Database" for the session
db: List[Service] = [
    {"name": "Auth-Service", "status": "Healthy"},
    {"name": "Payment-Gateway", "status": "Latency High"}
]

@app.get("/")
def health_check():
    return {"status": "Systems Operational", "version": "2.0.1"}

@app.get("/services")
def get_services():
    return db

@app.post("/services")
def add_service(service: Service):
    db.append(service.dict())
    return {"message": "Service logged successfully"}