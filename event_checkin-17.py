# === Stage 17: Добавь группировку записей по категориям ===
# Project: EventCheckin
def categorize_records(records, categories):
    result = {cat: [] for cat in categories}
    for rec in records:
        if 'category' in rec and rec['category'] in result:
            result[rec['category']].append(rec)
        else:
            result['uncategorized'].append(rec)
    return result

def display_categorized(categorized):
    print("=== Отметки по категориям ===")
    for cat, items in categorized.items():
        if not items:
            continue
        print(f"\n[{cat}] ({len(items)} записей)")
        for item in items:
            print(f"  - {item.get('name', 'Без имени')} | Статус: {item.get('status', 'Неизвестный')}")

# Пример использования
all_records = [
    {"id": "r1", "name": "Анна Иванова", "ticket_id": "t1", "category": "VIP", "status": "Прошел"},
    {"id": "r2", "name": "Борис Петров", "ticket_id": "t2", "category": "Генерал", "status": "Ожидание"},
    {"id": "r3", "name": "Виктория Сидорова", "ticket_id": "t3", "category": None, "status": "Прошел"},
]

categories = ["VIP", "Генерал"]
categorized = categorize_records(all_records, categories)
display_categorized(categorized)
