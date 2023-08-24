def calculate_porcentage_change(previous_value: int, current_value: int) -> int:
    if previous_value == 0:
        return None
    return round(((current_value - previous_value) / previous_value) * 100)
