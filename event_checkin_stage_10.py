# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: EventCheckin
def export_state_to_json():
    import json
    from datetime import datetime
    state = {
        "timestamp": datetime.utcnow().isoformat(),
        "events": events,
        "guests": guests,
        "stats": stats
    }
    return json.dumps(state, indent=2, ensure_ascii=False)
