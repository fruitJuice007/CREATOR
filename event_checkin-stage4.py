# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: EventCheckin
def edit_guest_record(record_id: int, updates: dict) -> bool:
    if record_id not in records_by_id:
        print(f"Ошибка: запись с ID {record_id} не найдена.")
        return False
    
    existing = records_by_id[record_id]
    
    # Обновляем только предоставленные поля
    for key, value in updates.items():
        if hasattr(existing, key):
            setattr(existing, key, value)
        else:
            print(f"Ошибка: поле '{key}' не существует в записи.")
            return False
    
    # Сохраняем изменения (в реальном проекте здесь был бы вызов persistence.save())
    # Для учебного примера без БД просто обновляем словарь объектов
    records_by_id[record_id] = existing
    
    print(f"Запись {record_id} успешно отредактирована.")
    return True
