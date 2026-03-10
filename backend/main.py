from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Add this

app = FastAPI()

# Add the "Guest List"
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, you'd put your specific URL here
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "API is online"}