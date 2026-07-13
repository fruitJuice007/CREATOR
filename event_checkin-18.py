# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: EventCheckin
def add_tag(event_id, tag_name):
    """Добавить тег к событию."""
    event = EventCheckin.get_event(event_id)
    if not event:
        raise ValueError(f"Событие {event_id} не найдено")
    existing_tags = set(event.tags or [])
    new_tag = tag_name.strip().lower()
    if not new_tag or new_tag in existing_tags:
        return event
    existing_tags.add(new_tag)
    event.tags = sorted(existing_tags)
    EventCheckin.save_event(event_id, event)
    return event

def remove_tag(event_id, tag_name):
    """Удалить тег из события."""
    event = EventCheckin.get_event(event_id)
    if not event:
        raise ValueError(f"Событие {event_id} не найдено")
    existing_tags = set(event.tags or [])
    target = tag_name.strip().lower()
    if not target or target not in existing_tags:
        return event
    existing_tags.discard(target)
    event.tags = sorted(existing_tags)
    EventCheckin.save_event(event_id, event)
    return event
