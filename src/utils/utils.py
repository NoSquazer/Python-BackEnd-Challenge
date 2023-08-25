def calculate_porcentage(previous_value: int, current_value: int) -> int:
    if previous_value == 0:
        return 0
    return round(((current_value - previous_value) / previous_value) * 100)
