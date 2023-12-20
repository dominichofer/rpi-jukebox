"""Tests for the Jukebox class."""
import unittest
from rpi_jukebox import Jukebox
from rpi_jukebox.logger import FakeLogger
from rpi_jukebox.music_player import FakeMusicPlayer

class FakeButton:
    def __init__(self):
        self.when_pressed = lambda: None

    def press(self):
        self.when_pressed()


class JukeBoxTest(unittest.TestCase):
    def test_buton_press(self):
        # Arrange
        tracks = ["track0", "track1", "track2"]
        music_player = FakeMusicPlayer()
        buttons = [FakeButton(), FakeButton(), FakeButton()]
        logger = FakeLogger()
        Jukebox(tracks, music_player, buttons, logger)

        # Act
        buttons[1].press()

        # Assert
        self.assertIn("track1", music_player.played_tracks)
        self.assertIn("Pressed 1", logger.messages)
