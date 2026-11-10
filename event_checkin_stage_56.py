# === Stage 56: Добавь массовое обновление выбранных записей ===
# Project: EventCheckin
def bulk_update_records(records, new_value):
    if not records:
        print("Нет выбранных записей для обновления")
        return
    for record in records:
        record['status'] = new_value
    print(f"Обновлено {len(records)} записей на статус: {new_value}")
