# Python
from typing import List, Optional
from datetime import datetime

# Pydantic
from pydantic import BaseModel, EmailStr, UUID4, Field


class MonthResume(BaseModel):
    active_clients: int
    percentage_active_change: float
    signups_per_month: int
    percentage_signup_change: float
    cancellations_per_month: int
    percentage_cancellation_change: float
    inactivations_per_month: int
    percentage_inactivation_change: float
