import pyttsx3
import requests

import constants as const

from checkConnection import is_connected_to_internet


class TTSEngine:
    def __init__(self, lang="uk") -> None:
        self.language: str = lang
        self.online: bool = is_connected_to_internet()
        self.engine: pyttsx3.Engine = pyttsx3.init()
        voices: object = self.engine.getProperty("voices")
        for voice in voices:  # type: ignore
            if not self.language in voice.languages[0]: continue
            self.engine.setProperty("voice", voice.id)
            break

    def tts(self, text: str, output_file: str = "output.mp3") -> str:
        self.online = is_connected_to_internet()
        if self.online:
            self.tts_google(text, output_file)
        else:
            self.tts_pyttsx3(text, output_file)
        return output_file

    def tts_pyttsx3(self, text: str, output_file: str = "output.mp3") -> str:
        self.engine.save_to_file(text, output_file)
        self.engine.runAndWait()
        return output_file

    def tts_google(self, text: str, output_file: str) -> None:
        params: dict = {
            "ie": "UTF-8",
            "q": text,
            "tl": self.language,
            "client": "tw-ob",
        }
        headers: dict = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(const.GOOGLE_TTS, params=params, headers=headers)
        if response.status_code != 200:
            raise Exception("Online TTS failed")
        with open(output_file, "wb") as f:
            f.write(response.content)
