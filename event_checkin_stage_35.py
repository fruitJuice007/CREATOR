# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: EventCheckin
def suggest_next_action(current_state):
    actions = {
        "no_data": "Сначала введите данные: название события, дату, количество гостей.",
        "event_only": "Добавьте список гостей и начните отметки.",
        "guests_only": "Создайте статусы и добавьте статистику.",
        "all_ready": "Попробуйте выгрузить статистику в отчёт или добавить новый статус.",
        "partial_stats": "Заполните недостающую статистику для полной картины.",
    }
    if current_state.get("event") is None:
        return actions["no_data"]
    if current_state.get("guests") is None:
        return actions["event_only"]
    if current_state.get("stats") is None:
        return actions["guests_only"]
    if current_state.get("statuses") is None:
        return actions["all_ready"]
    return actions["partial_stats"]
