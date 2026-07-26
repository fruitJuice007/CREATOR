# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: EventCheckin
def demo():
    print("=== Demo: EventCheckin ===")
    event = Event()
    for i in range(20):
        guest = Guest(name=f"Guest {i}", email=f"guest{i}@mail.com", phone="+7 900 " + str(i).zfill(8))
        ticket = Ticket(number=str(i), price=50 + i * 10, status="active")
        guest.set_ticket(ticket)
        event.add_guest(guest)

    for i in range(3):
        group = Group(name=f"Group {i}")
        for j in range(3):
            member = Guest(name=f"M{i}{j}", email=f"{i}_{j}@mail.com", phone="+7 901 " + str(i * 100 + j).zfill(8))
            ticket = Ticket(number=f"grp{i}-{j}", price=25, status="active")
            member.set_ticket(ticket)
            group.add_member(member)
        event.add_group(group)

    print(f"Total guests: {event.get_guest_count()}")
    print(f"Total groups: {len(event.groups)}")
    for g in event.groups:
        print(f"  Group '{g.name}': {len(g.members)} members, tickets: {[m.ticket.number for m in g.members]}")

    event.checkin(0)
    event.checkin(1)
    event.checkin(2)

    stats = event.get_stats()
    print(f"\nStats: checked={stats['checked']}, total={stats['total']}")

    print("\n=== Demo finished ===")
