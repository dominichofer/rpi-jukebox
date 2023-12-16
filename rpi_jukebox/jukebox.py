"""Jukebox module"""

class Jukebox:
    "Jukebox"

    def __init__(
        self, tracks: list[str], music_player, playing_light, buttons, logger
    ) -> None:
        self.tracks = tracks
        self.music_player = music_player
        self.playing_light = playing_light
        self.buttons = buttons
        self.logger = logger
        self.is_playing = False

        # Register buttons
        for i, button in enumerate(self.buttons):
            button.when_pressed = lambda i=i: self.press(i)

    def press(self, index: int) -> None:
        "Play a track"
        if self.is_playing:
            self.logger.log(f"Pressed {index} while playing")
        else:
            self.logger.log(f"Pressed {index}")
            self.is_playing = True
            self.playing_light.on()
            self.music_player.play(self.tracks[index])
            self.playing_light.off()
            self.is_playing = False
