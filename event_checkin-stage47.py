# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: EventCheckin
def demo():
    print("=" * 60)
    print("DEMO: EventCheckin — полный сценарий")
    print("=" * 60)

    event = Event(name="TechConf 2025", venue="Moscow Center", capacity=100)
    print(f"Создано событие: {event.name} ({event.venue})\n")

    ticket = Ticket(guest_name="Алексей Иванов", ticket_type="VIP", event=event)
    ticket.status = "ПРОВЕРЕН"
    ticket.checked_at = datetime(2025, 3, 15, 14, 30)
    print(f"Билет: {ticket.guest_name}, {ticket.ticket_type} — {ticket.status}")
    print(f"  Статистика: {ticket.stats}\n")

    ticket2 = Ticket(guest_name="Мария Петрова", ticket_type="STD", event=event)
    ticket2.status = "В ОЖИДАНИИ"
    print(f"Билет: {ticket2.guest_name}, {ticket2.ticket_type} — {ticket2.status}\n")

    checkin = Checkin(guest_name="Олег Сидоров", event=event, status="ПРОВЕРЕН",
                       checked_at=datetime(2025, 3, 15, 14, 35), notes="Пришёл на 5 мин раньше")
    print(f"Проверка: {checkin.guest_name} — {checkin.status} ({checkin.checked_at})")
    print(f"  Статистика: {checkin.stats}\n")

    print("Список гостей на событие:")
    for g in event.guests:
        print(f"  • {g.name} ({g.get_status()})")

    print("\nОтчёт по билетам:")
    for t in ticket_list:
        print(f"  • {t.guest_name}: {t.ticket_type}, статус={t.status}")

    print("\nОтчёт по спискам гостей:")
    for lst in event.guest_lists:
        print(f"  • {lst.name}: {lst.get_guests_count()} гостей")

    print("\nОтчёт по спискам гостей (альтернативный):")
    for lst in event.guest_lists_alt:
        print(f"  • {lst.name}: {lst.get_guests_count()} гостей")

    event.save()
    print(f"\n✅ Событие сохранено: {event.id}")
    print(f"   Путь: {event.path}")
    print(f"\n🎉 Демо завершено!")
