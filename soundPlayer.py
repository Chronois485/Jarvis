import pygame
import time

from os import path, remove


class SoundPlayer:
    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()

    def play(self, sound: str) -> None:
        if not path.exists(sound):
            return
        sound_effect = pygame.mixer.Sound(sound)
        sound_effect.play()
        time.sleep(sound_effect.get_length())

    def play_and_delete(self, sound: str) -> None:
        if not path.exists(sound):
            return
        self.play(sound)
        remove(sound)
