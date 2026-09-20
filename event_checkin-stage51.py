# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: EventCheckin
class AuditLog:
    def __init__(self):
        self._entries = []

    def record(self, entity: str, action: str, details: dict):
        self._entries.append({
            "entity": entity,
            "action": action,
            "details": details,
            "timestamp": datetime.now().isoformat(),
        })

    def get_entries(self, entity: str = None, action: str = None):
        entries = self._entries
        if entity:
            entries = [e for e in entries if e["entity"] == entity]
        if action:
            entries = [e for e in entries if e["action"] == action]
        return entries
