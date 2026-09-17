# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: EventCheckin
def print_stats(events):
    if not events:
        print("Нет данных для статистики.")
        return
    total_guests = sum(len(e['guests']) for e in events)
    checked_in = sum(len(e['guests']) for e in events if e['checked_in'])
    print(f"Всего гостей: {total_guests}")
    print(f"Отметили: {checked_in}")
    print(f"Осталось: {total_guests - checked_in}")
    print(f"Процент: {checked_in/total_guests*100:.1f}%")

def find_event(events, name):
    for e in events:
        if e['name'].lower() == name.lower():
            return e
    return None

def add_event(events, name, capacity):
    if not capacity or capacity <= 0:
        print("Вместимость должна быть положительной.")
        return None
    for e in events:
        if e['name'].lower() == name.lower():
            print(f"Событие '{name}' уже существует.")
            return e
    return {'name': name, 'capacity': capacity, 'guests': [], 'checked_in': []}
