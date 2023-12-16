from signal import pause
from gpiozero import LED, Button
from .music_player import MusicPlayer
from .logger import Logger
from .jukebox import Jukebox


if __name__ == "__main__":
    try:
        logger = Logger("log.txt")

        logger.log("Initializing status light")
        status_light = LED(2)
        status_light.off()
        logger.log("Status light ready")

        tracks = ["track1.mp3", "track2.mp3", "track3.mp3"]
        logger.log(f"Tracks: {tracks}")

        logger.log("Initializing music player")
        music_player = MusicPlayer()
        logger.log("Music player ready")

        logger.log("Initializing playing light")
        playing_light = LED(2)
        logger.log("Playing light ready")

        logger.log("Initializing buttons")
        buttons = [Button(3), Button(4), Button(5)]
        logger.log("Buttons ready")

        logger.log("Initializing jukebox")
        jukebox = Jukebox(tracks, music_player, playing_light, buttons, logger)
        logger.log("Jukebox ready")

        logger.log("Running jukebox")
        status_light.on()
        pause()
    except Exception as e:
        print(f"Error: {e}")
        status_light.blink(0.1, 0.1)
