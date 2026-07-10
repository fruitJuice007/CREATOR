# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: EventCheckin
def monthly_stats(events, guests):
    """Return dict {month: {'total_guests': int, 'checked_in': int}}."""
    stats = {}
    for e in events:
        if not hasattr(e, 'date') or not isinstance(e.date, datetime):
            continue
        year = e.date.year
        month = e.date.month
        key = (year, month)
        if key not in stats:
            stats[key] = {'total_guests': 0, 'checked_in': 0}
    for g in guests:
        if not hasattr(g, 'event') or not isinstance(g.event, dict):
            continue
        evt = g.event
        if not hasattr(evt, 'date') or not isinstance(evt.date, datetime):
            continue
        key = (evt.date.year, evt.date.month)
        stats[key]['total_guests'] += 1
    for g in guests:
        if hasattr(g, 'checked_in') and g.checked_in:
            # assume guest has a reference to event date
            if not hasattr(g, 'event_date') or not isinstance(g.event_date, datetime):
                continue
            key = (g.event_date.year, g.event_date.month)
            stats[key]['checked_in'] += 1
    return stats
