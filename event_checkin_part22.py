# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: EventCheckin
def check_expired_reminders():
    """Проверяет просроченные напоминания для гостей с запланированными отметками."""
    now = datetime.now()
    expired_guests = []
    
    for guest in guests_with_checkins:
        if hasattr(guest, 'reminder_date') and guest.reminder_date is not None:
            if guest.reminder_date < now:
                expired_guests.append({
                    'name': guest.name,
                    'event': getattr(guest, 'event', 'Неизвестное'),
                    'days_overdue': (now - guest.reminder_date).days
                })
    
    return expired_guests
