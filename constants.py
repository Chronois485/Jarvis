from settingsManager import SettingsManager
from enum import Enum


# Enums

class RecognitionModels(Enum):
    UK = "./models/uk-ua"
    EN = "./models/en-us"


class Languages(Enum):
    UKRAINIAN = "uk-UA"
    ENGLISH = "en-US"


# Settings
SETTINGS_MANAGER: SettingsManager = SettingsManager("./settings")

# Files
COMMANDS: str = "./commands.json"

# URLs
GOOGLE: str = "https://google.com"
GOOGLE_FIND: str = "https://www.google.com/search?q={promt}"
GOOGLE_TTS: str = "https://translate.google.com/translate_tts"

# Audio
AUDIO_RATE: int = 16000
AUDIO_WIDTH: int = 2

# Jarvis answers
ANSWER_WHAT_DATE: str = "{name}, Сьогодні {date}"
ANSWER_WHAT_TIME: str = "{name}, Зараз {time}"
ANSWER_OPEN: str = "Відкриваю, {name}"
ANSWER_EXIT: str = "До побачення, {name}"
