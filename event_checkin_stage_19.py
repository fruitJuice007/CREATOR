# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: EventCheckin
def archive_event_records(event_id, cutoff_date=None):
    """Archive check-in records for an event that are older than the cutoff date."""
    import json
    from datetime import datetime
    if not os.path.exists('checkins.json'):
        return []
    with open('checkins.json', 'r') as f:
        records = json.load(f)
    filtered = [rec for rec in records if rec['event_id'] == event_id]
    archived = []
    if cutoff_date is None:
        cutoff_date = datetime(1970, 1, 1)
    for rec in filtered:
        checkin_time = datetime.fromisoformat(rec.get('checkin_time', '1970-01-01'))
        if checkin_time < cutoff_date:
            archived.append({**rec, 'archived': True})
    with open('checkins.json', 'w') as f:
        json.dump(records, f, indent=2)
    return archived
