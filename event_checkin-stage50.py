# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: EventCheckin
def print_report(event: Event) -> None:
    """Выводит отчёт по событию: количество гостей, статусы и статистику."""
    total = len(event.guests)
    checked = sum(1 for g in event.guests if g.status == "checked")
    print(f"Событие: {event.name}")
    print(f"Всего гостей: {total}")
    print(f"Отмечено: {checked} ({checked / max(total, 1) * 100:.1f}%)")
    if event.guests:
        print(f"Первый гость: {event.guests[0].name}")
        print(f"Последний гость: {event.guests[-1].name}")
    print()

def print_help() -> None:
    """Выводит список доступных команд программы."""
    print("Доступные команды:")
    print("  add <имя> <билет> <список> <статус> — добавить гостя")
    print("  list — показать всех гостей")
    print("  report — показать отчёт")
    print("  help — показать эту справку")
    print("  quit — завершить работу")
    print()
