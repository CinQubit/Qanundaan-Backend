from fastapi import APIRouter
from . import endpoint1, endpoint2  # Correct relative import

router = APIRouter()

router.include_router(endpoint1.router, tags=["Endpoint 1"])
router.include_router(endpoint2.router, tags=["Endpoint 2"])
