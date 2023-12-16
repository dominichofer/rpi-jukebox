"""Music player module"""
import pygame


class MusicPlayer:
    "Pygame music player"

    def __init__(self) -> None:
        pygame.mixer.init()

    def play(self, track: str) -> None:
        "Play a track"
        pygame.mixer.music.load(track)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass


class FakeMusicPlayer:
    "Stub for MusicPlayer"

    def __init__(self) -> None:
        self.played_tracks : list = []

    def play(self, track: str) -> None:
        "Play a track"
        self.played_tracks.append(track)
