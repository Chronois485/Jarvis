import json
import os
from re import I

import speech_recognition as sr
from vosk import KaldiRecognizer, Model

from conventor import convert_audio_data_to_raw
from internetManager import InternetManager


class Recognizer:
    def __init__(self, model_path: str = "", language: str = "en-US") -> None:
        self.recognizer_google = sr.Recognizer()
        self.language: str = language
        self.language_vosk: str = self.language[:2]
        self.model = None
        self.internet_manager: InternetManager = InternetManager()
        if model_path and os.path.exists(model_path):
            self.model = Model(model_path)
            self.recognizer_vosk = KaldiRecognizer(self.model, 16000)

    def listen(self) -> sr.AudioData | None:
        with sr.Microphone() as source:
            auido = self.recognizer_google.listen(source)
        return auido if type(auido) == sr.AudioData else None

    def recognize_google(self, audio: sr.AudioData) -> str:
        try:
            text: str = self.recognizer_google.recognize_google(audio, language=self.language)  # type: ignore
            return text
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            return str(e)

    def recognize_vosk(self, audio: sr.AudioData) -> str:
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
        if not audio:
            return ""
        return (
            self.recognize_google(audio)
            if self.internet_manager.is_connected_to_internet()
            else self.recognize_vosk(audio)
        )
