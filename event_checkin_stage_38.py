# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: EventCheckin
import unittest

class TestEdgeCases(unittest.TestCase):
    def test_ticket_not_found(self):
        checkin = EventCheckin('Event')
        checkin.add_ticket('T1', 'Alice', 'VIP')
        checkin.add_ticket('T2', 'Bob', 'STANDARD')
        with self.assertRaises(KeyError):
            checkin.checkin('T3', 'Charlie')

    def test_guest_already_checked_in(self):
        checkin = EventCheckin('Event')
        checkin.add_ticket('T1', 'Alice', 'VIP')
        checkin.checkin('T1', 'Alice')
        with self.assertRaises(ValueError):
            checkin.checkin('T1', 'Alice')

    def test_checkin_with_zero_count(self):
        checkin = EventCheckin('Event')
        checkin.add_ticket('T1', 'Alice', 'VIP', 0)
        checkin.checkin('T1', 'Alice')
        self.assertEqual(checkin.get_count('T1'), 0)

    def test_checkin_with_negative_count(self):
        checkin = EventCheckin('Event')
        checkin.add_ticket('T1', 'Alice', 'VIP', -1)
        checkin.checkin('T1', 'Alice')
        self.assertEqual(checkin.get_count('T1'), -1)

    def test_checkin_with_empty_name(self):
        checkin = EventCheckin('Event')
        checkin.add_ticket('T1', 'Alice', 'VIP')
        with self.assertRaises(ValueError):
            checkin.checkin('T1', '')

    def test_checkin_with_none_status(self):
        checkin = EventCheckin('Event')
        checkin.add_ticket('T1', 'Alice', None)
        checkin.checkin('T1', 'Alice')
        self.assertIsNone(checkin.get_status('T1'))

    def test_checkin_with_empty_event_name(self):
        checkin = EventCheckin('')
        checkin.add_ticket('T1', 'Alice', 'VIP')
        checkin.checkin('T1', 'Alice')
        self.assertEqual(checkin.get_count('T1'), 1)

    def test_checkin_with_special_characters(self):
        checkin = EventCheckin('Special & <event>')
        checkin.add_ticket('T1', 'Alice', 'VIP')
        checkin.checkin('T1', 'Alice')
        self.assertEqual(checkin.get_count('T1'), 1)

    def test_checkin_with_unicode(self):
        checkin = EventCheckin('Событие')
        checkin.add_ticket('T1', 'Алиса', 'VIP')
        checkin.checkin('T1', 'Алиса')
        self.assertEqual(checkin.get_count('T1'), 1)

if __name__ == '__main__':
    unittest.main()
