import speech_recognition as sr


def convert_audio_data_to_raw(audio_data: sr.AudioData) -> bytes:
    return audio_data.get_raw_data(convert_rate=16000, convert_width=2)
