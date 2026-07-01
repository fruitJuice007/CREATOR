# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: EventCheckin
import json, os

DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"events": [], "guests": []}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {"events": [], "guests": []}

def save_data(data):
    temp_file = DATA_FILE + ".tmp"
    try:
        with open(temp_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        os.replace(temp_file, DATA_FILE)
    except IOError:
        if os.path.exists(temp_file):
            os.remove(temp_file)

def get_guest_by_id(guests, guest_id):
    for g in guests:
        if g.get("id") == guest_id:
            return g
    return None

def add_event(event_data):
    data = load_data()
    event_data["id"] = len(data["events"]) + 1
    data["events"].append(event_data)
    save_data(data)

def register_guest(guest_name, guest_id=None, ticket_type="general"):
    if not guest_id:
        guest_id = len(load_data()["guests"]) + 1
    data = load_data()
    new_guest = {"id": guest_id, "name": guest_name, "ticket_type": ticket_type, "status": "pending"}
    data["guests"].append(new_guest)
    save_data(data)

def checkin_guest(guest_id):
    data = load_data()
    for event in data["events"]:
        if not event.get("checkins"):
            continue
        guest = get_guest_by_id(data["guests"], guest_id)
        if not guest:
            return False, "Guest not found"
        if any(c["guest_id"] == guest_id for c in event["checkins"]):
            return True, "Already checked in"
        event.setdefault("checkins", []).append({"guest_id": guest_id, "status": "checked_in"})
        save_data(data)
        return True, f"{guest['name']} checked in to Event #{event['id']}"
    return False, "No active events found"

def get_statistics():
    data = load_data()
    total_guests = len(data["guests"])
    checked_in_count = sum(len(e.get("checkins", [])) for e in data["events"] if e.get("checkins"))
    pending_count = sum(1 for g in data["guests"] if not any(c["guest_id"] == g["id"] and c["status"] == "checked_in" for e in data["events"] for c in e.get("checkins", [])))
    return {"total_guests": total_guests, "checked_in_count": checked_in_count, "pending_count": pending_count}
