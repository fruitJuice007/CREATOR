# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: EventCheckin
def remind_me(task, date):
    """Напоминание: задача + дата выполнения (строка)."""
    reminder = {
        'task': task,
        'date': date,
        'done': False,
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M'),
    }
    reminders.append(reminder)
    print(f"Напоминание добавлено: {task} — {date}")


def show_reminders():
    """Показать все напоминания, отсортированные по дате."""
    if not reminders:
        print("Нет напоминаний.")
        return
    sorted_rems = sorted(reminders, key=lambda r: r['date'])
    for i, r in enumerate(sorted_rems, 1):
        status = "✅" if r['done'] else "⬜"
        print(f"{i}. {status} {r['task']} — {r['date']} ({r['created_at']})")


def mark_reminder_done(index):
    """Отметить напоминание как выполненное по индексу (начиная с 1)."""
    if not reminders:
        print("Нет напоминаний.")
        return
    sorted_rems = sorted(reminders, key=lambda r: r['date'])
    idx = index - 1
    if idx < len(sorted_rems):
        sorted_rems[idx]['done'] = True
        print(f"Напоминание '{sorted_rems[idx]['task']}' отмечено как выполнено.")


# Пример использования (не обязательный, можно закомментировать):
if __name__ == '__main__':
    remind_me("Сдать отчёт", "2025-12-31")
    remind_me("Купить молоко", "2026-01-05")
    show_reminders()
