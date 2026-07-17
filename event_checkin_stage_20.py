# === Stage 20: Добавь восстановление записей из архива ===
# Project: EventCheckin
import json, os

def restore_from_archive(archive_path):
    if not os.path.exists(archive_path):
        return 0
    with open(archive_path, 'r', encoding='utf-8') as f:
        records = json.load(f)
    count = len(records)
    for r in records:
        try:
            from eventcheckin import GuestCheckin
            guest = GuestCheckin(r['name'], r.get('email'), r.get('ticket'))
            guest.status = r.get('status', 'checked_in')
            guest.notes = r.get('notes', '')
            if r.get('special_list'):
                from eventcheckin import SpecialList, CheckinList
                sl = SpecialList(r['special_list'])
                cl = CheckinList(sl)
                guest.list = cl
        except Exception:
            pass
    return count

def archive_records(records):
    path = 'archives/checkins.json'
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
    return len(records)

def export_statistics():
    stats = {'total': 0, 'checked_in': 0, 'waiting': 0}
    try:
        from eventcheckin import GuestCheckin
        for guest in GuestCheckin.all_guests():
            stats['total'] += 1
            if hasattr(guest, 'status') and guest.status == 'checked_in':
                stats['checked_in'] += 1
            elif hasattr(guest, 'status') and guest.status == 'waiting':
                stats['waiting'] += 1
    except Exception:
        pass
    return stats
