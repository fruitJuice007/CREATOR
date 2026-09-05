# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: EventCheckin
def main():
    parser = argparse.ArgumentParser(prog="eventcheckin", description="Гостевая система отметок события")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # --- checkin ---
    p_checkin = sub.add_parser("checkin", help="Отметить гостя")
    p_checkin.add_argument("--guest-id", required=True, help="ID гостя")
    p_checkin.add_argument("--ticket-id", help="ID билета (для привязки)")
    p_checkin.add_argument("--list-id", help="ID списка гостей")
    p_checkin.add_argument("--status", default="checked_in", help="Статус: checked_in, waiting, left")

    # --- checkin-batch ---
    p_batch = sub.add_parser("checkin-batch", help="Пакетная отметка гостей из CSV")
    p_batch.add_argument("--file", required=True, help="Путь к CSV-файлу (guest_id, status, ...)")

    # --- status ---
    p_status = sub.add_parser("status", help="Сверка статусов гостей")
    p_status.add_argument("--guest-id", help="ID гостя")

    # --- stats ---
    p_stats = sub.add_parser("stats", help="Вывод статистики")

    args = parser.parse_args()
    if hasattr(args, "checkin"):
        checkin(args)
    elif hasattr(args, "checkin_batch"):
        checkin_batch(args)
    elif hasattr(args, "status"):
        status(args)
    elif hasattr(args, "stats"):
        stats()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
