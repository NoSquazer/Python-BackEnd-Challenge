# Python
from dateutil.relativedelta import relativedelta
from datetime import datetime

# SrcUtilities
from src.utils.utils import calculate_porcentage


class Services:
    @staticmethod
    def _clients_count(db, filter_query: dict) -> int:
        clients = db.clientes.find(filter_query)
        clients_count = len(list(clients))
        return clients_count

    @staticmethod
    def _get_month_range(month: datetime) -> datetime:
        end_date = month + relativedelta(months=1)
        return end_date

    @staticmethod
    def _get_previous_month_range(month: datetime) -> datetime:
        previous_month = month - relativedelta(months=1)
        return previous_month

    @classmethod
    def get_active_clients(cls, db, month: datetime) -> int:
        end_date = cls._get_month_range(month=month)

        active_clients_count = cls._clients_count(
            db,
            {
                "status": "activo",
                "last_subscription_date": {"$gte": month, "$lt": end_date},
            },
        )

        return active_clients_count

    @classmethod
    def get_active_members_porcentage_change_prev_month(
        cls, db, month: datetime
    ) -> int:
        previous_month = cls._get_previous_month_range(month)

        previous_month_clients_count = cls._clients_count(
            db,
            {
                "status": "activo",
                "last_subscription_date": {
                    "$gte": previous_month,
                    "$lt": month,
                },
            },
        )

        current_month_clients_count = cls.get_active_clients(db, month)

        porcentage_active_change = calculate_porcentage(
            previous_month_clients_count, current_month_clients_count
        )

        return porcentage_active_change

    @classmethod
    def get_new_clients(cls, db, month: datetime):
        end_date = cls._get_month_range(month)
        new_clients_count = cls._clients_count(
            db,
            {
                "history": {
                    "$elemMatch": {
                        "date_created": {"$gte": month, "$lt": end_date},
                        "event": "alta",
                    }
                }
            },
        )

        return new_clients_count

    @classmethod
    def get_new_clients_porcentage_change_prev_month(cls, db, month: datetime) -> int:
        previous_month = cls._get_previous_month_range(month)

        previous_new_clients_count = cls._clients_count(
            db,
            {
                "history": {
                    "$elemMatch": {
                        "date_created": {
                            "$gte": previous_month,
                            "$lt": month,
                        },
                        "event": "alta",
                    }
                }
            },
        )

        current_new_clients_count = cls.get_new_clients(db, month=month)

        new_clients_change_porcentage = calculate_porcentage(
            previous_new_clients_count, current_new_clients_count
        )

        return new_clients_change_porcentage

    @classmethod
    def get_deregistrations(cls, db, month: datetime) -> int:
        end_date = cls._get_month_range(month)

        deregistrations_clients_count = cls._clients_count(
            db,
            {
                "history": {
                    "$elemMatch": {
                        "date_created": {"$gte": month, "$lt": end_date},
                        "event": "baja",
                    }
                }
            },
        )

        return deregistrations_clients_count

    @classmethod
    def get_deregistrations_porcentage_change_prev_month(
        cls, db, month: datetime
    ) -> int:
        previous_month = cls._get_previous_month_range(month)

        previous_month_deregistrations_clients_count = cls._clients_count(
            db,
            {
                "history": {
                    "$elemMatch": {
                        "date_created": {
                            "$gte": previous_month,
                            "$lt": month,
                        },
                        "event": "alta",
                    }
                }
            },
        )

        current_month_deregistrations_clients_count = cls.get_deregistrations(
            db, month=month
        )

        deregistrations_clients_porcentage = calculate_porcentage(
            previous_month_deregistrations_clients_count,
            current_month_deregistrations_clients_count,
        )

        return deregistrations_clients_porcentage

    @classmethod
    def get_inactivations_without_termination(cls, db, month: datetime) -> int:
        end_date = cls._get_month_range(month)

        inactivations_without_termination_count = cls._clients_count(
            db,
            {
                "history": {
                    "$elemMatch": {
                        "date_created": {"$gte": month, "$lt": end_date},
                        "event": {"$ne": "baja"},
                    }
                }
            },
        )

        return inactivations_without_termination_count

    @classmethod
    def get_inactivations_without_termination_porcentage_change_prev_month(
        cls, db, month: datetime
    ) -> int:
        previous_month = cls._get_previous_month_range(month)

        previous_inactivations_without_termination_count = cls._clients_count(
            db,
            {
                "history": {
                    "$elemMatch": {
                        "date_created": {
                            "$gte": previous_month,
                            "$lt": month,
                        },
                        "event": {"$ne": "baja"},
                    }
                }
            },
        )

        current_inactivations_without_termination_count = (
            cls.get_inactivations_without_termination(db, month=month)
        )

        inactivations_without_termination_change_porcentage = calculate_porcentage(
            previous_inactivations_without_termination_count,
            current_inactivations_without_termination_count,
        )

        return inactivations_without_termination_change_porcentage

    @classmethod
    def get_month_resume_data(cls, db, month: datetime) -> dict:
        return {
            "active_clients": cls.get_active_clients(db=db, month=month),
            "active_members_porcentage_change_prev_month": cls.get_active_members_porcentage_change_prev_month(
                db=db, month=month
            ),
            "new_clients": cls.get_new_clients(db=db, month=month),
            "new_clients_porcentage_change_prev_month": cls.get_new_clients_porcentage_change_prev_month(
                db=db, month=month
            ),
            "deregistrations": cls.get_deregistrations(db=db, month=month),
            "deregistrations_porcentage_change_prev_month": cls.get_deregistrations_porcentage_change_prev_month(
                db=db, month=month
            ),
            "inactivations_without_termination": cls.get_inactivations_without_termination(
                db=db, month=month
            ),
            "inactivations_without_termination_porcentage_change_prev_month": cls.get_inactivations_without_termination_porcentage_change_prev_month(
                db=db, month=month
            ),
            "active_members_porcentage_change_prev_month": cls.get_active_members_porcentage_change_prev_month(
                db=db, month=month
            ),
        }


month_resume_service = Services
