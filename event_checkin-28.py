# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: EventCheckin
def print_metrics(data):
    total_guests = len(data.get("guests", []))
    checked_in = sum(1 for g in data["guests"] if g["status"] == "checked_in")
    not_checked_in = sum(1 for g in data["guests"] if g["status"] == "not_checked_in")

    total_seats = len(data.get("seats", []))
    used_seats = len([s for s in data["seats"] if s["occupied"]])
    available_seats = total_seats - used_seats

    vip_count = sum(1 for g in data["guests"] if g.get("vip", False))
    regular_count = total_guests - vip_count

    tickets_total = len(data.get("tickets", []))
    tickets_used = sum(1 for t in data["tickets"] if t["used"])
    tickets_free = tickets_total - tickets_used

    stats = f"""
📊 Статистика:
Всего гостей: {total_guests} | Прошедших: {checked_in} | Оставшихся: {not_checked_in}
Кресла: всего {total_seats}, занято {used_seats}, свободно {available_seats}
VIP-гости: {vip_count} | Обычные: {regular_count}
Билеты: всего {tickets_total}, использовано {tickets_used}, свободно {tickets_free}
"""
    print(stats)
