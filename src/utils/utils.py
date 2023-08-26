def calculate_porcentage(previous_value: int, current_value: int) -> int:
    if previous_value == 0:
        return 0
    return round(((current_value - previous_value) / previous_value) * 100)


def calculate_total_porcentage(total_amount: int, total_all: int) -> int:
    if total_amount == 0:
        return 0
    return round((total_amount / total_all) * 100)
