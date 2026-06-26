# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: EventCheckin
def sort_guests(criteria='date'):
    if criteria == 'date':
        return sorted(guest_list, key=lambda x: x['checkin_time'], reverse=True)
    elif criteria == 'priority':
        return sorted(guest_list, key=lambda x: x.get('priority', 0), reverse=True)
    elif criteria == 'name':
        return sorted(guest_list, key=lambda x: x['guest_name'].lower())
    else:
        return guest_list
