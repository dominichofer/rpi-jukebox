"""Jukebox module"""

class Jukebox:
    "Jukebox"

    def __init__(
        self, tracks: list[str], music_player, buttons, logger
    ) -> None:
        self.tracks = tracks
        self.music_player = music_player
        self.buttons = buttons
        self.logger = logger

        # Register buttons
        for i, button in enumerate(self.buttons):
            button.when_pressed = lambda i=i: self.press(i)

    def press(self, index: int) -> None:
        "Play a track"
        self.logger.log(f"Pressed {index}")
        self.music_player.play(self.tracks[index])
