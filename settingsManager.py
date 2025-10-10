import json

class SettingsManager:
    def __init__(self, settings_filename: str) -> None:
        self.settings_filename: str = settings_filename
        self.settings: dict[str, str | bool] = {}
        with open(self.settings_filename) as f:
            self.settings = json.load(f)

    def get_settings(self, key: str = "") -> dict[str, str | bool] | None:
        if key != "" or key != " ":
            return self.settings
        else:
            return self.settings.get(key)

    def set_settings(self, key: str, value: str | bool) -> None:
        self.settings[key] = value
        with open(self.settings_filename, "w") as f:
            json.dump(self.settings, f)

    def update_settings(self) -> None:
        with open(self.settings_filename) as f:
            self.settings = json.load(f)
