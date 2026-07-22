# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: EventCheckin
def console_table(data, headers):
    widths = [len(str(h)) for h in headers]
    for row in data:
        for i, val in enumerate(row):
            if len(str(val)) > widths[i]:
                widths[i] = len(str(val))
    lines = []
    total_w = sum(widths) + 2 * (len(headers) - 1)
    sep = '+' + '+'.join('-' * (w + 2) for w in widths) + '+'
    lines.append(sep)
    hdr = '|' + '|'.join(f'{str(h):<{w}}' for h, w in zip(headers, widths)) + '|'
    lines.append(hdr)
    lines.append(sep)
    for row in data:
        line = '|' + '|'.join(f'{str(v):<{w}}' for v, w in zip(row, widths)) + '|'
        lines.append(line)
    lines.append(sep)
    print('\n'.join(lines))
