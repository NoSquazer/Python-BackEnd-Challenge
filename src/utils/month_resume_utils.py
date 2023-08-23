def calculate_percentage_change(previous_value, current_value):
    if previous_value == 0:
        return None
    return ((current_value - previous_value) / previous_value) * 100
