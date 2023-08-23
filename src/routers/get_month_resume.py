from typing import List
from fastapi import APIRouter, Depends, Body
from datetime import datetime
from fastapi.responses import JSONResponse
from bson.json_util import dumps

from src.services.month_resume_service import month_resume_service

from src.dependencies import get_db


get_month_resume_router = APIRouter()


@get_month_resume_router.post("/a")
def get_month_resume(
    company: str = Body(...), month: datetime = Body(...), db=Depends(get_db)
) -> JSONResponse:
    active_clients = month_resume_service.active_clients(
        db=db, company=company, month=month
    )
    porcentage_active_change = month_resume_service.percentage_active_change(
        db=db, company=company, month=month
    )

    response_data = {
        "active_clients": active_clients,
        "porcentage_active_change": porcentage_active_change,
    }

    return JSONResponse(content=response_data)
