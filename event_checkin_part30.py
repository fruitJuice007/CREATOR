# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: EventCheckin
import json, os

def load_profiles():
    path = "eventcheckin_profiles.json"
    if not os.path.exists(path):
        return {"admin": {"name": "Администратор", "role": "admin"}, "guest": {"name": "Гость", "role": "guest"}}
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_profiles(profiles):
    with open("eventcheckin_profiles.json", 'w', encoding='utf-8') as f:
        json.dump(profiles, f, ensure_ascii=False, indent=2)

def get_current_profile():
    profiles = load_profiles()
    if not profiles:
        return None
    for p in profiles.values():
        if "last_login" in p and p["last_login"]:
            return p
    return list(profiles.values())[0]
