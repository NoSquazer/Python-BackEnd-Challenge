# Python
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from calendar import monthrange
from bson import ObjectId

# SrcUtilities
from src.utils.utils import calculate_porcentage


class Services:
    @staticmethod
    def _calculate_total_revenue(
        db, company: str, month: datetime, source_filters: list[str]
    ) -> float:
        end_date = month + relativedelta(days=month.day)

        revenue_docs = db.boletas.find(
            {
                "date_created": {"$gt": month, "$lt": end_date},
                "merchant_id": {"$eq": ObjectId(company)},
                "source": {"$in": source_filters},
                "charges_detail.final_price": {"$exists": True},
            }
        )

        total_revenue = sum(
            doc["charges_detail"]["final_price"]
            for doc in revenue_docs
            if isinstance(doc["charges_detail"]["final_price"], (int, float))
        )

        return total_revenue

    @classmethod
    def get_total_revenue(cls, db, company: str, month: datetime) -> int:
        return cls._calculate_total_revenue(
            db,
            company,
            month,
            [
                "checkout",
                "checkout3",
                "checkout_miclub",
                "recurring_charges",
                "recurring_miclub",
            ],
        )

    @classmethod
    def get_total_recurrence_revenue(cls, db, company: str, month: datetime) -> float:
        return cls._calculate_total_revenue(
            db,
            company,
            month,
            ["recurring_charges", "recurring_miclub"],
        )

    @classmethod
    def get_total_altas_revenue(cls, db, company: str, month: datetime) -> float:
        return cls._calculate_total_revenue(
            db,
            company,
            month,
            ["checkout", "checkout3", "checkout_miclub"],
        )

    @classmethod
    def get_total_revenue_variation(cls, db, company: str, month: datetime) -> float:
        current_month_revenue = cls.get_total_revenue(db, company, month)

        previous_month = month - relativedelta(months=1)
        previous_month = previous_month.replace(
            day=monthrange(previous_month.year, previous_month.month)[1]
        )
        previous_month_revenue = cls.get_total_revenue(db, company, previous_month)

        revenue_variation = calculate_porcentage(
            previous_month_revenue, current_month_revenue
        )
        return revenue_variation

    @classmethod
    def get_total_recurrence_revenue_variation(
        cls, db, company: str, month: datetime
    ) -> float:
        current_month_recurrence_revenue = cls.get_total_recurrence_revenue(
            db, company, month
        )

        previous_month = month - relativedelta(months=1)
        previous_month = previous_month.replace(
            day=monthrange(previous_month.year, previous_month.month)[1]
        )
        previous_month_recurrence_revenue = cls.get_total_recurrence_revenue(
            db, company, previous_month
        )

        total_recurrence_revenue = calculate_porcentage(
            previous_month_recurrence_revenue, current_month_recurrence_revenue
        )

        return total_recurrence_revenue

    @classmethod
    def get_total_altas_revenue_variation(
        cls, db, company: str, month: datetime
    ) -> float:
        current_month_altas_revenue = cls.get_total_altas_revenue(db, company, month)

        previous_month = month - relativedelta(months=1)
        previous_month = previous_month.replace(
            day=monthrange(previous_month.year, previous_month.month)[1]
        )
        previous_month_altas_revenue = cls.get_total_altas_revenue(
            db, company, previous_month
        )

        total_altas_revenue = calculate_porcentage(
            previous_month_altas_revenue, current_month_altas_revenue
        )

        return total_altas_revenue

    @classmethod
    def get_billing_metrics(cls, db, company: str, month: datetime) -> dict:
        billing_metrics = {
            "total_revenue": cls.get_total_revenue(db, company, month),
            "total_revenue_variation": cls.get_total_altas_revenue_variation(
                db, company, month
            ),
            "total_recurrence_revenue": cls.get_total_recurrence_revenue(
                db, company, month
            ),
            "total_recurrence_variation": cls.get_total_recurrence_revenue_variation(
                db, company, month
            ),
            "total_altas_revenue": cls.get_total_altas_revenue(db, company, month),
            "total_altas_variation": cls.get_total_altas_revenue_variation(
                db, company, month
            ),
        }

        return billing_metrics


month_summary_service = Services
