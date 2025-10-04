import json
import os

import speech_recognition as sr
from vosk import KaldiRecognizer, Model

from checkConnection import is_connected_to_internet
from conventor import convert_audio_data_to_raw


class Recognizer:
    def __init__(self, model_path: str = "", language: str = "en-US") -> None:
        self.recognizer_google = sr.Recognizer()
        self.language: str = language
        self.language_vosk: str = self.language[:2]
        self.model = None
        if model_path and os.path.exists(model_path):
            self.model = Model(model_path)
            self.recognizer_vosk = KaldiRecognizer(self.model, 16000)

    def listen(self):
        with sr.Microphone() as source:
            auido = self.recognizer_google.listen(source)
        return auido

    def recognize_google(self, audio) -> str:
        try:
            text: str = self.recognizer_google.recognize_google(audio, language=self.language)  # type: ignore
            return text
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            return str(e)

    def recognize_vosk(self, audio) -> str:
        if self.model:
            data: bytes = convert_audio_data_to_raw(audio)
            if self.recognizer_vosk.AcceptWaveform(data):
                result = json.loads(self.recognizer_vosk.Result())
            else:
                result = json.loads(self.recognizer_vosk.FinalResult())
            return result.get("text", "")
        else:
            return ""

    def recognize(self, audio) -> str:
        return (
            self.recognize_google(audio)
            if is_connected_to_internet()
            else self.recognize_vosk(audio)
        )


if __name__ == "__main__":
    recognizer = Recognizer()
    print(f"Testing speech recognition for english wia google")
    print(f"You said: {recognizer.recognize_google(recognizer.listen())}")
    del recognizer
    recognizer = Recognizer(language="uk-UA")
    print(f"Testing speech recognition for ukrainian wia google")
    print(f"You said: {recognizer.recognize_google(recognizer.listen())}")
    del recognizer
    recognizer = Recognizer("./models/recognizer/en-us")
    print(f"Testing speech recognition for english wia vosk")
    print(f"You said: {recognizer.recognize_vosk(recognizer.listen())}")
    del recognizer
    recognizer = Recognizer("./models/recognizer/uk-ua", language="uk-UA")
    print(f"Testing speech recognition for ukrainian wia vosk")
    print(f"You said: {recognizer.recognize_vosk(recognizer.listen())}")

