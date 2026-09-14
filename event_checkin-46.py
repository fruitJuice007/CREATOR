# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: EventCheckin
import json

MIGRATION_VERSION = {"major": 1, "minor": 46}

def migrate_to_v1_46(data):
    if "event" not in data:
        data["event"] = {
            "name": "EventCheckin",
            "description": "Guest check-in system with tickets, lists, statuses, and stats.",
            "venue": "Conference Hall",
            "date": "2025-07-25",
            "max_guests": 500,
            "is_active": True,
        }
    if "tickets" not in data:
        data["tickets"] = []
    if "checkin_lists" not in data:
        data["checkin_lists"] = []
    if "statuses" not in data:
        data["statuses"] = {
            "registered": {"label": "Registered", "color": "green"},
            "checked_in": {"label": "Checked In", "color": "blue"},
            "vip": {"label": "VIP", "color": "gold"},
            "pending": {"label": "Pending", "color": "gray"},
            "late": {"label": "Late", "color": "red"},
        }
    if "stats" not in data:
        data["stats"] = {"total_checked_in": 0, "total_registered": 0, "total_pending": 0, "total_late": 0, "total_vip": 0}
    if "history" not in data:
        data["history"] = []
    return data

def save_migration(data, filename="eventcheckin.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Migrated to version {MIGRATION_VERSION['major']}.{MIGRATION_VERSION['minor']} and saved to {filename}.")

if __name__ == "__main__":
    import os
    if os.path.exists("eventcheckin.json"):
        with open("eventcheckin.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {}
    data = migrate_to_v1_46(data)
    save_migration(data)
