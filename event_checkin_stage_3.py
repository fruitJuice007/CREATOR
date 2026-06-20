# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: EventCheckin
class EventCheckin:
    def __init__(self):
        self.records = []
    
    def add_record(self, ticket_id, guest_name, status="pending"):
        record = {"ticket_id": ticket_id, "guest_name": guest_name, "status": status}
        self.records.append(record)
        return len(self.records)
