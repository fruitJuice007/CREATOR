# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: EventCheckin
TEMPLATES = {}

def register_template(name, fields):
    TEMPLATES[name] = fields

def get_template(name):
    return TEMPLATES.get(name)

def checkin_with_template(name, guest_name, guest_email=None, ticket_id=None, list_name=None, note=None):
    tpl = get_template(name)
    if tpl is None:
        raise ValueError(f"Template '{name}' not found")
    record = {
        "guest_name": guest_name,
        "guest_email": guest_email or "",
        "ticket_id": ticket_id or 0,
        "list_name": list_name or "",
        "note": note or "",
        "status": "checked_in",
        "timestamp": datetime.now().isoformat(),
    }
    for key, value in tpl.items():
        record[key] = value
    return record
