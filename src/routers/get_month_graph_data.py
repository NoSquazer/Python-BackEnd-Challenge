# Python
from datetime import datetime

# FastAPI
from fastapi import APIRouter, Depends, Query
from fastapi.responses import JSONResponse

# SrcUtilities
from src.utils.schemas import MonthBillingData
from src.services.month_billing_data_service import month_billing_data_service
from src.dependencies import get_db


get_month_graph_data_router = APIRouter()


@get_month_graph_data_router.get("/graph-data", response_model=MonthBillingData)
def get_month_billing_data(
    month: str = Query(..., description="Month in MM-YYYY format"),
    company: str = Query(..., description="Business name or identifier"),
    db=Depends(get_db),
) -> JSONResponse:
    try:
        month_date = datetime.strptime(month, "%m-%Y")
        if month_date >= datetime(2023, 7, 1):
            return JSONResponse(
                content={"error": "Month cannot be after July 2023."},
                status_code=400,
            )

        response_data = month_billing_data_service.get_month_billing_data(
            db=db, company=company, month=month_date
        )

        return JSONResponse(content=response_data)

    except ValueError:
        return JSONResponse(
            content={"error": "Invalid date format. Please use MM-YYYY format."},
            status_code=400,
        )
