# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: EventCheckin
import json, os
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Guest:
    name: str
    ticket_id: int
    status: str = "pending"
    notes: list[str] = field(default_factory=list)

def init_demo_data() -> dict:
    if not os.path.exists("eventcheckin.json"):
        demo_guests = [
            Guest("Алексей Иванов", 101, "checked_in"),
            Guest("Мария Петрова", 102, "pending"),
            Guest("Дмитрий Сидоров", 103, "rejected", ["Нет билета"]),
        ]
        with open("eventcheckin.json", "w", encoding="utf-8") as f:
            json.dump([g.__dict__ for g in demo_guests], f, ensure_ascii=False, indent=2)
    return {"guests": []}

def load_data() -> dict:
    try:
        with open("eventcheckin.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return init_demo_data()
