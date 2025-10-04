from os import path, remove

from audioplayer import AudioPlayer

from conventor import convert_mp3_to_wav


def play(sound: str) -> None:
    if not path.exists(sound):
        return
    if path.splitext(sound)[1] == ".mp3":
        sound = convert_mp3_to_wav(sound)  # type: ignore
    player: AudioPlayer = AudioPlayer(sound)
    player.play()


def play_and_delete(sound: str) -> None:
    if not path.exists(sound):
        return
    play(sound)
    remove(sound)


if __name__ == "__main__":
    print("Testing audioPlayer.play()")
    play("/home/chronois/Files/python/jarvis/test.mp3")
    print("Testing audioPlayer.play_and_delete()")
    play_and_delete("test.mp3")

