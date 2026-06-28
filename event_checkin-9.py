# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: EventCheckin
import json, sys, os
from pathlib import Path

def load_initial_data(json_string: str) -> dict:
    """Загружает начальные данные из JSON-строки в структуру проекта."""
    try:
        raw = json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return {}

    if not isinstance(raw, dict):
        print("JSON должен содержать объект корня.")
        return {}

    data = {
        "events": raw.get("events", []),
        "guests": raw.get("guests", []),
        "tickets": raw.get("tickets", []),
        "config": raw.get("config", {})
    }

    # Валидация обязательных полей
    if not data["events"]:
        print("Предупреждение: список событий пуст.")
    
    return data

# Пример использования (раскомментируйте для теста):
if __name__ == "__main__":
    sample_json = '''
    {
      "events": [{"id": 1, "name": "Концерт", "date": "2024-12-31"}],
      "guests": [],
      "tickets": [],
      "config": {"timezone": "UTC+3"}
    }'''
    
    initial_data = load_initial_data(sample_json)
    print(f"Загружено {len(initial_data['events'])} событий.")
