# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: EventCheckin
def export_report(events, guests, stats):
    lines = []
    lines.append("=== EventCheckin Report ===")
    lines.append(f"Total events: {len(events)}")
    lines.append(f"Total guests: {len(guests)}")
    lines.append(f"Checked-in: {stats['checked_in']}")
    lines.append(f"Checked-out: {stats['checked_out']}")
    lines.append(f"Pending: {stats['pending']}")
    lines.append(f"Total tickets: {stats['total_tickets']}")
    lines.append(f"Total lists: {stats['total_lists']}")
    lines.append(f"Total statuses: {stats['total_statuses']}")
    for event in events:
        lines.append(f"\n--- Event: {event['title']} ---")
        lines.append(f"  Date: {event['date']}")
        lines.append(f"  Location: {event['location']}")
        lines.append(f"  Guests checked in: {len(event['guests']['checked_in'])}")
        lines.append(f"  Guests checked out: {len(event['guests']['checked_out'])}")
        lines.append(f"  Tickets: {len(event['tickets'])}")
        lines.append(f"  Lists: {len(event['lists'])}")
        lines.append(f"  Statuses: {len(event['statuses'])}")
    return "\n".join(lines)
