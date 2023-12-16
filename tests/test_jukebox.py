"""Tests for the Jukebox class."""
import unittest
from rpi_jukebox import Jukebox
from rpi_jukebox.logger import FakeLogger
from rpi_jukebox.music_player import FakeMusicPlayer


class FakeLight:
    def __init__(self):
        self.is_on = False

    def on(self):
        self.is_on = True

    def off(self):
        self.is_on = False


class FakeButton:
    def __init__(self):
        self.when_pressed = lambda: None

    def press(self):
        self.when_pressed()


class JukeBoxTest(unittest.TestCase):
    def test_press_when_not_playing(self):
        # Arrange
        tracks = ["track0", "track1", "track2"]
        music_player = FakeMusicPlayer()
        playing_light = FakeLight()
        buttons = [FakeButton(), FakeButton(), FakeButton()]
        logger = FakeLogger()
        Jukebox(tracks, music_player, playing_light, buttons, logger)

        # Act
        buttons[1].press()

        # Assert
        self.assertIn("track1", music_player.played_tracks)
        self.assertFalse(playing_light.is_on)
        self.assertIn("Pressed 1", logger.messages)

    def test_press_when_playing(self):
        # Arrange
        buttons = [FakeButton(), FakeButton(), FakeButton()]

        class PressingMusicPlayer:
            def __init__(self) -> None:
                self.played_tracks : list = []

            def play(self, track: str) -> None:
                self.played_tracks.append(track)
                buttons[2].press()

        tracks = ["track0", "track1", "track2"]
        music_player = PressingMusicPlayer()
        playing_light = FakeLight()
        logger = FakeLogger()
        Jukebox(tracks, music_player, playing_light, buttons, logger)

        # Act
        buttons[1].press()

        # Assert
        self.assertIn("track1", music_player.played_tracks)
        self.assertNotIn("track2", music_player.played_tracks)
        self.assertFalse(playing_light.is_on)
        self.assertIn("Pressed 1", logger.messages)
        self.assertIn("Pressed 2 while playing", logger.messages)

    def test_lights_while_playing(self):
        # Arrange
        tracks = ["track0", "track1", "track2"]
        playing_light = FakeLight()

        class AssertingMusicPlayer(unittest.TestCase):
            def play(self, _):
                self.assertTrue(playing_light.is_on)

        music_player = AssertingMusicPlayer()
        buttons = [FakeButton(), FakeButton(), FakeButton()]
        logger = FakeLogger()
        Jukebox(tracks, music_player, playing_light, buttons, logger)

        # Act
        buttons[1].press()

        # Assert
        self.assertFalse(playing_light.is_on)
