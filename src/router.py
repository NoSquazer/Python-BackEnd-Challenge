# FastAPI
from fastapi import APIRouter

# SrcUtilities
from src.routers.get_month_resume import get_month_resume_router
from src.routers.get_month_billing import get_month_billing_router
from src.routers.get_month_billing_summary import get_month_billing_summary_router
from src.routers.get_month_porcentage_metrics import get_month_porcentage_metrics_router


api_router = APIRouter()

api_router.include_router(
    get_month_resume_router,
    prefix="/month",
    tags=["Get month resume data"],
)

api_router.include_router(
    get_month_billing_router,
    prefix="/month",
    tags=["Get month billing data"],
)

api_router.include_router(
    get_month_billing_summary_router,
    prefix="/month",
    tags=["Get month billing summary data"],
)

api_router.include_router(
    get_month_porcentage_metrics_router,
    prefix="/month",
    tags=["Get month porcentage metrics data"],
)
