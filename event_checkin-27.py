# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: EventCheckin
def reset_demo_data(store):
    store['events'] = []
    store['tickets'] = []
    store['guest_lists'] = {}
    store['checkins'] = []
    store['statuses'] = {'pending': 0, 'checked_in': 0}
    return store

def clear_state():
    """Reset all data and status counters to initial state."""
    reset_demo_data(s)
