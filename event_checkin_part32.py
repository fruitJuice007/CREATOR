# === Stage 32: Добавь журнал действий пользователя ===
# Project: EventCheckin
class AuditLog:
    def __init__(self):
        self.entries = []

    def log(self, actor, action, target=None, details=None):
        self.entries.append({
            "actor": actor,
            "action": action,
            "target": target,
            "details": details,
            "timestamp": datetime.now().isoformat(),
        })

    def get_recent(self, limit=10):
        return self.entries[-limit:]

    def get_by_action(self, action):
        return [e for e in self.entries if e["action"] == action]
