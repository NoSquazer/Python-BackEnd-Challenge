# Python
from typing import Optional
from datetime import datetime

# Pydantic
from pydantic import BaseModel


class MonthResume(BaseModel):
    active_clients: Optional[int] = 0
    active_members_percentage_change_prev_month: Optional[int] = 0
    new_clients: Optional[int] = 0
    new_clients_porcentage_change_prev_month: Optional[int] = 0
    deregistrations: Optional[int] = 0
    deregistrations_porcentage_change_prev_month: Optional[int] = 0
    inactivations_without_termination: Optional[int] = 0
    inactivations_without_termination_percentage_change_prev_month: Optional[int] = 0


class MonthBilling(BaseModel):
    day: Optional[datetime] = "0000-00-00 00:00:00"
    altas_count: Optional[datetime] = 0
    recurrency_count: Optional[datetime] = 0


class MonthBillingSummary(BaseModel):
    total_revenue_current: Optional[int] = 0
    total_revenue_variation: Optional[int] = 0
    recurrences_revenue_current: Optional[int] = 0
    recurrences_revenue_variation: Optional[int] = 0
    altas_revenue_current: Optional[int] = 0
    altas_revenue_variation: Optional[int] = 0


class MonthPorcentageMetrics(BaseModel):
    recurring_charges: Optional[int] = 0
    checkout: Optional[int] = 0
    checkout_miclub: Optional[int] = 0
    recurring_miclub: Optional[int] = 0
    local_level: Optional[int] = 0
    plus_level: Optional[int] = 0
    total_level: Optional[int] = 0
