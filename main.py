from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import router as api_v1_router
from app.database.connection import database
from config import settings

app = FastAPI()

# CORS middleware to handle cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include your API routers
app.include_router(api_v1_router, prefix="/api/v1")

# Startup event to connect to the database when the Application starts
@app.on_event("startup")
async def startup_event():
    await database.connect()

# Shutdown event to disconnect from the database when the Application stops
@app.on_event("shutdown")
async def shutdown_event():
    await database.disconnect()
