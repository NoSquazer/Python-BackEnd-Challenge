# Python
from typing import List, Optional
from datetime import datetime

# Pydantic
from pydantic import BaseModel, EmailStr, UUID4, Field


class MonthResume(BaseModel):
    active_clients: Optional[int] = 0
    active_members_percentage_change_prev_month: Optional[int] = 0
    new_clients: Optional[int] = 0
    new_clients_porcentage_change_prev_month: Optional[int] = 0
    deregistrations: Optional[int] = 0
    deregistrations_porcentage_change_prev_month: Optional[int] = 0
    inactivations_without_termination: Optional[int] = 0
    inactivations_without_termination_percentage_change_prev_month: Optional[int] = 0


class MonthBillingData(BaseModel):
    active_clients: Optional[int] = 0
    active_members_percentage_change_prev_month: Optional[int] = 0
    new_clients: Optional[int] = 0
    new_clients_porcentage_change_prev_month: Optional[int] = 0
    deregistrations: Optional[int] = 0
    deregistrations_porcentage_change_prev_month: Optional[int] = 0
    inactivations_without_termination: Optional[int] = 0
    inactivations_without_termination_percentage_change_prev_month: Optional[int] = 0


class MonthBilling(BaseModel):
    total_revenue_current: Optional[int] = 0
    total_revenue_variation: Optional[int] = 0
    recurrences_revenue_current: Optional[int] = 0
    recurrences_revenue_variation: Optional[int] = 0
    altas_revenue_current: Optional[int] = 0
    ltas_revenue_variation: Optional[int] = 0
