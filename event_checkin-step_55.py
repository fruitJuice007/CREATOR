# === Stage 55: Добавь мягкую проверку дубликатов при создании записей ===
# Project: EventCheckin
def _find_duplicate_record(existing_records, new_values, key_fields):
    for record in existing_records:
        match = True
        for field in key_fields:
            if record.get(field) != new_values.get(field):
                match = False
                break
        if match:
            return record
    return None

def add_record_with_duplicate_check(existing_records, new_values, key_fields=None, tolerance=0.8):
    if key_fields is None:
        key_fields = list(new_values.keys())
    duplicate = _find_duplicate_record(existing_records, new_values, key_fields)
    if duplicate is not None:
        return None
    return dict(new_values)
