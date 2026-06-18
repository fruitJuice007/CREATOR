# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: EventCheckin
from typing import Optional, Dict, List
import re

class ValidationError(Exception):
    pass

def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_phone(phone: str) -> bool:
    cleaned = re.sub(r'[^\d]', '', phone)
    return len(cleaned) in [10, 11] and (cleaned.startswith('7') or cleaned.startswith('+7'))

class GuestTicket:
    def __init__(self, guest_name: str, email: str, ticket_id: Optional[str] = None):
        self._validate_inputs(guest_name, email)
        self.guest_name = guest_name.strip()
        self.email = email.lower().strip() if validate_email(email) else ''
        self.ticket_id = ticket_id or f"TICKET-{len(self.__class__.__dict__.get('instances', [])) + 1}"

    def _validate_inputs(self, name: str, email: str):
        if not name.strip():
            raise ValidationError("Имя гостя не может быть пустым.")
        if len(name) > 50:
            raise ValidationError("Имя слишком длинное (макс. 50 символов).")

class EventStats:
    def __init__(self):
        self.total_guests = 0
        self.checked_in_count = 0
        self.statuses: Dict[str, int] = {}

    def record_checkin(self, status: str) -> None:
        if not validate_phone(status.replace('-', '').replace(' ', '')):
            raise ValidationError("Неверный формат статуса (ожидался телефон).")
        self.checked_in_count += 1
        self.total_guests += 1
        self.statuses[status] = self.statuses.get(status, 0) + 1
