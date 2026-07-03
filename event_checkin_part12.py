# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: EventCheckin
def load_data_from_json(filepath):
    try:
        import json
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект корень")
        return {k: v for k, v in data.items() if isinstance(v, (list, dict))}
    except FileNotFoundError:
        print(f"Файл не найден: {filepath}")
        return {}
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return {}
