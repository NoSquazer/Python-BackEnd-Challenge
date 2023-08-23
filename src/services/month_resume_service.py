from dateutil.relativedelta import relativedelta
from datetime import datetime
from src.utils.month_resume_utils import calculate_percentage_change


class Services:
    def active_clients(db, company: str, month: datetime):
        end_date = month + relativedelta(months=1)
        filtered_clients = db.clientes.find(
            {"last_subscription_date": {"$gte": month, "$lt": end_date}}
        )
        active_subscriber_count = len(list(filtered_clients))

        return active_subscriber_count

    def percentage_active_change(db, *, company: str, month: datetime):
        previous_month = month - relativedelta(months=1)
        previous_month_end_date = previous_month + relativedelta(months=1)
        previous_month_clients = db.clientes.find(
            {
                "last_subscription_date": {
                    "$gte": previous_month,
                    "$lt": previous_month_end_date,
                }
            }
        )
        current_month_subscribers = Services.active_clients(
            db, company=company, month=month
        )
        previous_month_clients_count = len(list(previous_month_clients))
        porcentage_active_change = calculate_percentage_change(
            previous_month_clients_count, current_month_subscribers
        )

        return porcentage_active_change


month_resume_service = Services
