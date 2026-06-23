# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: EventCheckin
def delete_guest_record(guest_id: int) -> bool:
    """Удаление записи гостя по ID с обработкой отсутствия записи."""
    if not isinstance(guest_id, int):
        raise ValueError("guest_id должен быть целым числом")
    
    # Имитация поиска и удаления в структуре данных (списке словарей)
    records = get_all_guest_records()  # Предположим, что эта функция уже существует
    
    for i, record in enumerate(records):
        if record.get('id') == guest_id:
            del records[i]
            return True
            
    return False

def delete_event_record(event_id: int) -> bool:
    """Удаление записи события по ID с обработкой отсутствия."""
    if not isinstance(event_id, int):
        raise ValueError("event_id должен быть целым числом")
    
    events = get_all_events()  # Предположим, что эта функция уже существует
    
    for i, event in enumerate(events):
        if event.get('id') == event_id:
            del events[i]
            return True
            
    return False

def handle_missing_identifier(identifier_type: str, identifier_value) -> None:
    """Централизованная обработка отсутствующих идентификаторов."""
    valid_types = ['guest', 'event']
    
    if identifier_type not in valid_types:
        print(f"Ошибка: Неизвестный тип идентификатора '{identifier_type}'. Допустимые: {valid_types}")
        return
        
    if isinstance(identifier_value, int):
        # Попытка удаления (если контекст требует) или логирование
        if identifier_type == 'guest':
            delete_guest_record(identifier_value)
        else:
            delete_event_record(identifier_value)
