# FastAPI
from fastapi import APIRouter

# SrcUtilities
from src.routers.get_month_resume import get_month_resume_router
from src.routers.get_month_graph_data import get_month_graph_data_router
from src.routers.get_month_billing_data import get_month_billing_data_router
from src.routers.get_month_porcentage_metrics import get_month_porcentage_metrics_router


api_router = APIRouter()

api_router.include_router(
    get_month_resume_router,
    prefix="/month",
    tags=["Get month resume"],
)

api_router.include_router(
    get_month_graph_data_router,
    prefix="/month",
    tags=["Get month billing data"],
)

api_router.include_router(
    get_month_billing_data_router,
    prefix="/month",
    tags=["Get month summary data"],
)

api_router.include_router(
    get_month_porcentage_metrics_router,
    prefix="/month",
    tags=["Get month porcentage metrics data"],
)
