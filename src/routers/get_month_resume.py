# Python
from datetime import datetime

# FastAPI
from fastapi import APIRouter, Depends, Query
from fastapi.responses import JSONResponse

# SrcUtilities
from src.utils.schemas import MonthResume
from src.services.month_resume_service import month_resume_service
from src.dependencies import get_db


get_month_resume_router = APIRouter()


@get_month_resume_router.get("/resume", response_model=MonthResume)
def get_month_resume(
    month: str = Query(..., description="Month in MM-YYYY format"),
    company: str = Query(..., description="Business identifier"),
    db=Depends(get_db),
) -> JSONResponse:
    try:
        month_date = datetime.strptime(month, "%m-%Y")
        if month_date >= datetime(2023, 7, 1) or month_date <= datetime(2021, 12, 1):
            return JSONResponse(
                content={
                    "error": "Month cannot be before January 2022 or after July 2023."
                },
                status_code=400,
            )

        response_data = month_resume_service.get_month_resume_data(
            db=db, month=month_date
        )

        return JSONResponse(content=response_data)

    except ValueError:
        return JSONResponse(
            content={"error": "Invalid date format. Please use MM-YYYY format."},
            status_code=400,
        )
