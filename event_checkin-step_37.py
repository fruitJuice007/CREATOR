# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: EventCheckin
import unittest
from unittest.mock import patch


class TestEventCheckin(unittest.TestCase):
    def test_checkin_success(self):
        from event_checkin import Guest, GuestTicket, GuestList, GuestStatus, GuestCheckin
        ticket = GuestTicket("T001", "VIP")
        guest = Guest("Alice", "alice@example.com")
        guest.add_ticket(ticket)
        list1 = GuestList("VIP List", "vip@example.com")
        guest.add_list(list1)
        guest.checkin(GuestStatus.CHECKED_IN)
        self.assertEqual(guest.status, GuestStatus.CHECKED_IN)
        self.assertEqual(guest.ticket_count, 1)
        self.assertEqual(guest.list_count, 1)

    def test_checkin_multiple_guests(self):
        from event_checkin import Guest, GuestTicket, GuestList, GuestStatus, GuestCheckin
        ticket = GuestTicket("T002", "STD")
        guests = [Guest("Bob", "bob@example.com"), Guest("Charlie", "charlie@example.com")]
        for g in guests:
            g.add_ticket(ticket)
            g.checkin(GuestStatus.CHECKED_IN)
        self.assertEqual(len(guests), 2)
        for g in guests:
            self.assertEqual(g.status, GuestStatus.CHECKED_IN)

    def test_checkin_with_stats(self):
        from event_checkin import Guest, GuestTicket, GuestList, GuestStatus, GuestCheckin
        ticket = GuestTicket("T003", "STD")
        guest = Guest("Diana", "diana@example.com")
        guest.add_ticket(ticket)
        guest.checkin(GuestStatus.CHECKED_IN)
        stats = GuestCheckin.get_stats()
        self.assertEqual(stats["total_guests"], 1)
        self.assertEqual(stats["checked_in"], 1)

    def test_checkin_with_mocked_stats(self):
        from event_checkin import Guest, GuestTicket, GuestList, GuestStatus, GuestCheckin
        ticket = GuestTicket("T004", "VIP")
        guest = Guest("Eve", "eve@example.com")
        guest.add_ticket(ticket)
        guest.checkin(GuestStatus.CHECKED_IN)
        stats = GuestCheckin.get_stats()
        self.assertEqual(stats["total_guests"], 1)
        self.assertEqual(stats["checked_in"], 1)

    def test_checkin_with_ticket_types(self):
        from event_checkin import Guest, GuestTicket, GuestList, GuestStatus, GuestCheckin
        ticket = GuestTicket("T005", "STD")
        guest = Guest("Frank", "frank@example.com")
        guest.add_ticket(ticket)
        guest.checkin(GuestStatus.CHECKED_IN)
        stats = GuestCheckin.get_stats()
        self.assertEqual(stats["total_guests"], 1)
        self.assertEqual(stats["checked_in"], 1)


if __name__ == "__main__":
    unittest.main()
