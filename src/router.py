# FastAPI
from fastapi import APIRouter

# SrcUtilities
from src.routers.get_month_resume import get_month_resume_router
from src.routers.get_month_billing_data import get_month_billing_data_router


api_router = APIRouter()

api_router.include_router(
    get_month_resume_router,
    prefix="/month",
    tags=["Get month resume"],
)

api_router.include_router(
    get_month_billing_data_router,
    prefix="/month",
    tags=["Get month billing data"],
)
