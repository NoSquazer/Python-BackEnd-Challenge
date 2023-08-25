# Python
from datetime import datetime, timedelta
from calendar import monthrange


class Services:
    @staticmethod
    def _get_invoices_count(db, filter_query: dict) -> int:
        invoices = db.boletas.find(filter_query)
        invoices_count = len(list(invoices))

        return invoices_count

    @staticmethod
    def _get_num_days_in_month(month: datetime) -> datetime:
        num_days = monthrange(month.year, month.month)[1]
        return num_days

    @classmethod
    def get_altas_count(cls, db, company: str, start_date: datetime) -> int:
        end_date = start_date + timedelta(days=1)
        altas_count = cls._get_invoices_count(
            db,
            {
                "date_created": {"$gt": start_date, "$lt": end_date},
                "source": {"$in": ["checkout", "checkout3", "checkout_miclub"]},
            },
        )
        return altas_count

    @classmethod
    def get_recurrency_count(cls, db, company: str, start_date: datetime) -> int:
        end_date = start_date + timedelta(days=1)

        recurrency_count = cls._get_invoices_count(
            db,
            {
                "date_created": {"$gt": start_date, "$lt": end_date},
                "source": {"$in": ["recurring_charges", "recurring_miclub"]},
            },
        )
        return recurrency_count

    @classmethod
    def get_month_billing_data(cls, db, company: str, month: datetime) -> int:
        days_of_the_month = cls._get_num_days_in_month(month=month)

        data_list = [
            {
                "day": str(month.replace(day=day)),
                "altas_count": cls.get_altas_count(db, company, month.replace(day=day)),
                "recurrency_count": cls.get_recurrency_count(
                    db, company, month.replace(day=day)
                ),
            }
            for day in range(1, days_of_the_month + 1)
        ]

        return data_list


month_billing_data_service = Services
