# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: EventCheckin
class ProfileManager:
    def __init__(self):
        self.profiles = {}
        self.active_profile = None

    def add_profile(self, name, role="guest"):
        if not self.profiles or self.active_profile != name:
            self.profiles[name] = {"role": role}
            self.active_profile = name
        return self

    def switch_profile(self, name):
        if name in self.profiles and self.active_profile != name:
            self.active_profile = name
        return self

    def get_active_profile(self):
        return self.active_profile
