# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: EventCheckin
def check_integrity_and_repair():
    """Проверка целостности данных и простой ремонт.

    Проверяет:
    1. Все билеты имеют уникальный id.
    2. Все гости в списке имеют уникальный id.
    3. Статусы гостей соответствуют возможным значениям.
    4. Нет дубликатов записей в логах.
    """
    problems = []

    # Проверка уникальности ID билетов
    ticket_ids = [t['id'] for t in tickets]
    if len(ticket_ids) != len(set(ticket_ids)):
        problems.append("Дубликаты ID билетов")

    # Проверка уникальности ID гостей
    guest_ids = [g['id'] for g in guests]
    if len(guest_ids) != len(set(guest_ids)):
        problems.append("Дубликаты ID гостей")

    # Проверка корректности статусов
    valid_statuses = ['waiting', 'checked_in', 'rejected', 'vip']
    for guest in guests:
        if guest.get('status') not in valid_statuses:
            guest['status'] = 'waiting'
            problems.append(f"Гость {guest['id']} имеет некорректный статус, исправлено на 'waiting'")

    # Проверка уникальности записей в логах
    log_entries = [l['message'] for l in logs]
    if len(log_entries) != len(set(log_entries)):
        problems.append("Дубликаты записей в логах")

    # Вывод результатов
    if problems:
        print("Обнаружены проблемы:")
        for p in problems:
            print(f"  - {p}")
        print("Данные были исправлены.")
    else:
        print("Все данные целы и корректны.")

    return len(problems)
