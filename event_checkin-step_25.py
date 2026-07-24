# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: EventCheckin
def validate_date(date_str):
    """Проверяет корректность даты в формате YYYY-MM-DD, возвращает True/False."""
    try:
        year, month, day = map(int, date_str.split('-'))
        if not (1 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31):
            return False
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            days_in_month[2] = 29
        return day <= days_in_month[month]
    except Exception:
        return False
