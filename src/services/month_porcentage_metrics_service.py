# Python
from datetime import datetime, timedelta
from typing import List
from calendar import monthrange
from dateutil.relativedelta import relativedelta
from bson import ObjectId

# SrcUtilities
from src.utils.utils import calculate_total_porcentage


class Services:
    @staticmethod
    def _get_billing_docs_by_source(
        db, company: str, month: datetime, source: List[str]
    ) -> int:
        end_date = month + relativedelta(months=1)

        billing_docs = db.boletas.find(
            {
                "date_created": {"$gte": month, "$lt": end_date},
                "merchant_id": ObjectId(company),
                "source": {"$in": source},
                "status": "approved",
            }
        )

        total_amount = sum(doc["charges_detail"]["final_price"] for doc in billing_docs)

        return total_amount

    @staticmethod
    def _get_billing_docs_by_access_level(
        db, company: str, month: datetime, level: str
    ) -> int:
        end_date = month + relativedelta(months=1)

        billing_docs = db.planes.find(
            {
                "merchant_id": ObjectId(company),
                "nivel_de_acceso": level,
            }
        )

        total_amount = sum(doc["price"] for doc in billing_docs)

        return total_amount

    @classmethod
    def get_month_porcentages(cls, db, company: str, month: datetime) -> dict:
        recurring_charges_total_amount = cls._get_billing_docs_by_source(
            db, company, month, source=["recurring_charges"]
        )
        checkout_total_amount = cls._get_billing_docs_by_source(
            db, company, month, source=["checkout", "checkout3"]
        )
        checkout_miclub_total_amount = cls._get_billing_docs_by_source(
            db, company, month, source=["checkout_miclub"]
        )
        recurring_miclub_total_amount = cls._get_billing_docs_by_source(
            db, company, month, source=["recurring_miclub"]
        )

        local_level_total_amount = cls._get_billing_docs_by_access_level(
            db, company, month, level="Local"
        )
        plus_level_total_amount = cls._get_billing_docs_by_access_level(
            db, company, month, level="Plus"
        )
        total_level_total_amount = cls._get_billing_docs_by_access_level(
            db, company, month, level="Total"
        )

        total_all_sources = (
            recurring_charges_total_amount
            + checkout_total_amount
            + checkout_miclub_total_amount
            + recurring_miclub_total_amount
        )

        total_all_levels = (
            +local_level_total_amount
            + plus_level_total_amount
            + total_level_total_amount
        )

        percentages = {
            "recurring_charges": calculate_total_porcentage(
                recurring_charges_total_amount, total_all_sources
            ),
            "checkout": calculate_total_porcentage(
                checkout_total_amount, total_all_sources
            ),
            "checkout_miclub": calculate_total_porcentage(
                checkout_miclub_total_amount, total_all_sources
            ),
            "recurring_miclub": calculate_total_porcentage(
                recurring_miclub_total_amount, total_all_sources
            ),
            "local_level": calculate_total_porcentage(
                local_level_total_amount, total_all_levels
            ),
            "plus_level": calculate_total_porcentage(
                plus_level_total_amount, total_all_levels
            ),
            "total_level": calculate_total_porcentage(
                total_level_total_amount, total_all_levels
            ),
        }

        return percentages


month_porcentage_metrics_service = Services
