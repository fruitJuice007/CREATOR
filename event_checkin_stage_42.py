# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: EventCheckin
class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    HIDDEN = "\033[8m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

    @staticmethod
    def disable():
        Color.RED = Color.RESET
        Color.GREEN = Color.RESET
        Color.YELLOW = Color.RESET
        Color.BLUE = Color.RESET
        Color.MAGENTA = Color.RESET
        Color.CYAN = Color.RESET
        Color.WHITE = Color.RESET
        Color.BG_RED = Color.RESET
        Color.BG_GREEN = Color.RESET
        Color.BG_YELLOW = Color.RESET
        Color.BG_BLUE = Color.RESET
        Color.BG_MAGENTA = Color.RESET
        Color.BG_CYAN = Color.RESET
        Color.BG_WHITE = Color.RESET

    @staticmethod
    def enable():
        Color.disable()
        Color.RED = "\033[31m"
        Color.GREEN = "\033[32m"
        Color.YELLOW = "\033[33m"
        Color.BLUE = "\033[34m"
        Color.MAGENTA = "\033[35m"
        Color.CYAN = "\033[36m"
        Color.WHITE = "\033[37m"
        Color.BG_RED = "\033[41m"
        Color.BG_GREEN = "\033[42m"
        Color.BG_YELLOW = "\033[43m"
        Color.BG_BLUE = "\033[44m"
        Color.BG_MAGENTA = "\033[45m"
        Color.BG_CYAN = "\033[46m"
        Color.BG_WHITE = "\033[47m"
