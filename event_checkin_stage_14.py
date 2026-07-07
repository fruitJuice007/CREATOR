# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: EventCheckin
def generate_summary(events, guests):
    """Генерирует краткую сводку о текущем состоянии системы."""
    total = len(guests)
    checked_in = sum(1 for g in guests if g.checked_in)
    tickets_count = sum(len(e.tickets) for e in events)

    status_dist = {}
    for e in events:
        for t in e.tickets.values():
            s = t.status.name if hasattr(t, 'status') else str(getattr(t, 'status', '?'))
            status_dist[s] = status_dist.get(s, 0) + 1

    lines = [
        f"Сводка: {total} гостей, {checked_in} отметок",
        f"Билетов всего: {tickets_count}",
        "Статусы билетов:",
    ]
    for name, cnt in sorted(status_dist.items()):
        lines.append(f"  {name}: {cnt}")

    return "\n".join(lines)
