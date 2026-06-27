# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: EventCheckin
def main():
    print("=== EventCheckin CLI ===")
    while True:
        cmd = input("\n1. Список гостей\n2. Добавить гостя\n3. Проверить билет\n4. Статистика\n5. Выход\nВыберите действие (1-5): ").strip()
        if cmd == "1": print("Список гостей: Гость 1, Гость 2")
        elif cmd == "2": name = input("Имя гостя: "); print(f"Гость '{name}' добавлен.")
        elif cmd == "3": ticket = input("Номер билета: "); print(f"Билет {ticket}: Активен/Не найден")
        elif cmd == "4": print("Статистика: Всего гостей 2, Проверено билетов 1")
        elif cmd == "5": break
        else: print("Неверная команда.")

if __name__ == "__main__": main()
