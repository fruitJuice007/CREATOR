# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: EventCheckin
def search_guests(query: str, fields: list[str] = None) -> list[dict]:
    if not query:
        return []
    query_lower = query.lower()
    if fields is None:
        fields = ['name', 'ticket_id', 'email']
    results = [g for g in guests if any(query_lower in str(v).lower() for v in g.values())]
    return results
