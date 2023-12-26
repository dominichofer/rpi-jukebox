from signal import pause
from gpiozero import LED, Button
from rpi_jukebox import MusicPlayer, Logger, Jukebox


if __name__ == "__main__":
    try:
        logger = Logger("log.txt")
        logger.log("------ Started ------")

        tracks = [
            "help.mp3", # Top left
            "sky.mp3",
            "zjung.mp3",
            "charlotta.mp3",
            "tag.mp3", # Top right
            "tell.mp3", # Bottom left
            "radetzky.mp3",
            "fox.mp3",
            "kids.mp3",
            "twist.mp3", # Bottom right
        ]
        logger.log(f"Tracks: {tracks}")

        logger.log("Initializing music player")
        music_player = MusicPlayer()
        logger.log("Music player ready")

        logger.log("Initializing status light")
        status_light = LED(13)
        logger.log("Status light ready")

        logger.log("Initializing buttons")
        buttons = [
            Button(24), # Top left
            Button(25),
            Button(5),
            Button(6),
            Button(12), # Top right
            Button(4), # Bottom left
            Button(17),
            Button(27),
            Button(22),
            Button(23), # Bottom right
        ]
        logger.log("Buttons ready")

        logger.log("Initializing jukebox")
        jukebox = Jukebox(tracks, music_player, buttons, logger)
        logger.log("Jukebox ready")

        logger.log("Running jukebox")
        status_light.on()
        music_player.play("startup.mp3")
        pause()
    except Exception as e:
        print(f"Error: {e}")
        status_light.blink(0.1, 0.1)
        pause()
