from os import path, remove

import speech_recognition as sr
from pydub import AudioSegment


def convert_audio_data_to_raw(audio_data: sr.AudioData) -> bytes:
    return audio_data.get_raw_data(convert_rate=16000, convert_width=2)


def convert_mp3_to_wav(sound_file: str) -> str | None:
    if not path.exists(sound_file):
        return
    root, extention = path.splitext(sound_file)
    if extention != ".mp3":
        return
    sound = AudioSegment.from_mp3(sound_file)
    sound.export(f"{root}.wav", format="wav")
    remove(sound_file)
    return f"{root}.wav"

