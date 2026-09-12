# === Stage 45: Добавь восстановление из резервной копии ===
# Project: EventCheckin
def restore_from_backup(backup_path, log=None):
    """Восстановление данных из файла резервной копии.

    Формат: один JSON-объект со списком записей, записанный через
    json.dumps с отключённой сортировкой, чтобы сохранить порядок.

    Аргументы:
        backup_path (str) — путь к файлу резервной копии.
        log (object, optional) — объект с методом log(msg) для вывода.

    Возвращает:
        dict — словарь с ключами 'status' ('ok' или 'error') и 'message'.
    """
    try:
        import json
        with open(backup_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError("Резервная копия должна содержать список записей.")
        if log:
            log("Резервная копия восстановлена: {} записей из {}".format(len(data), backup_path))
        return {"status": "ok", "message": "Резервная копия успешно восстановлена", "record_count": len(data)}
    except Exception as e:
        msg = "Ошибка восстановления из {}: {}".format(backup_path, e)
        if log:
            log(msg)
        return {"status": "error", "message": msg}
