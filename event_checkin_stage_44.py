# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: EventCheckin
import shutil
import os
from datetime import datetime

def backup_data_file(data_path, backup_dir="backups"):
    if not os.path.exists(data_path):
        print(f"Файл данных не найден: {data_path}")
        return None
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"checkin_{timestamp}.bak")
    shutil.copy2(data_path, backup_path)
    print(f"Резервная копия создана: {backup_path}")
    return backup_path
