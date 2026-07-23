# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: EventCheckin
def format_record(record):
    """Компактный вывод записи гостя."""
    status = record.get("status", "UNKNOWN").upper()
    colors = {"WAITING": "\033[93m", "CHECKED_IN": "\033[92m", "REJECTED": "\033[31m"}
    color = colors.get(status, "")
    reset = "\033[0m"
    name = record.get("name", "?")
    ticket_id = record.get("ticket_id", "?")
    checkin_time = record.get("checkin_time", "N/A")
    notes = record.get("notes", "").strip() or "-"
    return f"{color}{status}{reset} | {name:<20s} | Ticket: {ticket_id:<15s} | Time: {checkin_time:<18s} | Notes: {notes}"

def print_records(records):
    """Вывод всех записей."""
    if not records:
        print("Нет записей.")
        return
    for r in records:
        print(format_record(r))
