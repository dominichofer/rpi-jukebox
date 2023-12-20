"""Music player module"""
from pygame import mixer


class MusicPlayer:
    "Pygame music player"

    def __init__(self) -> None:
        mixer.init()

    def play(self, track: str) -> None:
        "Play a track"
        mixer.music.load(track)
        mixer.music.play()


class FakeMusicPlayer:
    "Stub for MusicPlayer"

    def __init__(self) -> None:
        self.played_tracks : list = []

    def play(self, track: str) -> None:
        "Play a track"
        self.played_tracks.append(track)
