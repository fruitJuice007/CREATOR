# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: EventCheckin
def weekly_stats(events):
    """Calculate per-week check-in statistics grouped by date."""
    from collections import defaultdict
    
    week_groups = defaultdict(lambda: {"registered": 0, "total_invited": 0})
    
    for event in events:
        if not event.get("date"):
            continue
            
        # Get the week start (Monday) of the event's date
        d = datetime.date.fromisoformat(event["date"])
        day_of_week = d.weekday()
        week_start = d - timedelta(days=day_of_week)
        
        # Count unique guests registered for this event in this week
        guest_ids = set(guest.get("id") for guest in event.get("guests", []))
        
        week_groups[week_start.isoformat()]["registered"] += len(guest_ids)
        week_groups[week_start.isoformat()]["total_invited"] += len(event.get("guests", []))
    
    return week_groups
