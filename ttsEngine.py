import pyttsx3
import requests

from checkConnection import is_connected_to_internet


class TTSEngine:
    def __init__(self, lang="uk") -> None:
        self.language: str = lang
        self.online: bool = is_connected_to_internet()
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty("voices")
        for voice in voices:  # type: ignore
            if self.language in voice.languages[0]:  # .decode('utf-8'):
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
        url: str = "https://translate.google.com/translate_tts"
        params: dict = {
            "ie": "UTF-8",
            "q": text,
            "tl": self.language,
            "client": "tw-ob",
        }
        headers: dict = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, params=params, headers=headers)
        if response.status_code != 200:
            raise Exception("Online TTS failed")
        with open(output_file, "wb") as f:
            f.write(response.content)


if __name__ == "__main__":
    # tts = TTSEngine(lang="en")
    # print("Testing text-to-speech system in english, online")
    # tts.tts("Hello, I'm Jarvis", "online_english.mp3")
    # print("Testing text-to-speech system in english, offline")
    # tts.tts_pyttsx3("Hello, I'm Jarvis", "offline_english.mp3")
    # del tts
    # tts = TTSEngine(lang="uk")
    # print("Testing text-to-speech system in ukrainian, online")
    # tts.tts("Привіт, я Джарвіс", "online_ukrainian.mp3")
    # print("Testing text-to-speech system in ukrainian, offline")
    # tts.tts_pyttsx3("Привіт, я Джарвіс", "offline_ukrainian.mp3")
    # del tts
    tts = TTSEngine(lang="en")
    tts.tts("This is for playsound tests", "test.mp3")
    del tts
