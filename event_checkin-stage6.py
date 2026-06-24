# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: EventCheckin
def filter_records(status=None, category=None, tags=None):
    filtered = []
    for record in records:
        if status and record.status != status: continue
        if category and record.category != category: continue
        if tags is not None:
            record_tags = set(record.tags) if isinstance(record.tags, list) else {record.tags}
            if not any(tag in record_tags for tag in tags): continue
        filtered.append(record)
    return filtered
