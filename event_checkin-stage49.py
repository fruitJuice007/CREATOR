# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: EventCheckin
def main():
    """Финальная самопроверка: создание тестового события, гостей, билетов, списков, отметок и статистика."""
    event = Event("Тестовый вечер", "2026-05-15 19:00", max_guests=10)
    guest1 = Guest("Анна", "ann@example.com")
    guest2 = Guest("Борис", "boris@example.com")
    guest3 = Guest("Виктор", "victor@example.com")
    guest1.register()
    guest2.register()
    guest3.register()
    ticket = Ticket("A-001", "VIP", guest1, event)
    guest1.buy_ticket(ticket)
    ticket2 = Ticket("B-002", "Standard", guest2, event)
    guest2.buy_ticket(ticket2)
    guest3.buy_ticket(Ticket("C-003", "Standard", guest3, event))
    guest1.check_in()
    guest2.check_in()
    print(f"Событие: {event.name}")
    print(f"Гостей: {len(event.guests)}")
    print(f"Прошедших: {event.checkins_count}/{event.checkins_count}")
    print(f"Всего билетов: {sum(1 for g in event.guests if g.ticket)}")
    print(f"Статистика: {event.stats()}")

if __name__ == "__main__":
    main()
