from signal import pause
from gpiozero import LED, Button
from rpi_jukebox import MusicPlayer, Logger, Jukebox


if __name__ == "__main__":
    try:
        logger = Logger("log.txt")
        logger.log("------ Started ------")

        tracks = [
            "tag.mp3", # Top left
            "charlotta.mp3",
            "zjung.mp3",
            "sky.mp3",
            "help.mp3", # Bottom left
            "twist.mp3", # Top right
            "kids.mp3",
            "fox.mp3",
            "radetzky.mp3",
            "tell.mp3", # Bottom right
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
            Button(12), # Top left
            Button(6),
            Button(5),
            Button(25),
            Button(24), # Bottom left
            Button(23), # Top right
            Button(22),
            Button(27),
            Button(17),
            Button(4), # Bottom right
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
