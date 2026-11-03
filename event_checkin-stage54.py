# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: EventCheckin
class Favorites:
    def __init__(self):
        self.favorites = []

    def toggle_favorite(self, record):
        if record in self.favorites:
            self.favorites.remove(record)
        else:
            self.favorites.append(record)

    def is_favorite(self, record):
        return record in self.favorites

    def get_favorites(self):
        return self.favorites

    def quick_access(self):
        return self.favorites
