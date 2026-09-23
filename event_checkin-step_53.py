# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: EventCheckin
def import_records_from_file(filepath):
    """Import checkin records from a simple text file.
    
    File format: each line is 'name, ticket_type, status, timestamp'
    Returns list of dict records.
    """
    records = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split(',')
            if len(parts) != 4:
                continue
            records.append({
                'name': parts[0].strip(),
                'ticket_type': parts[1].strip(),
                'status': parts[2].strip(),
                'timestamp': parts[3].strip()
            })
    return records
