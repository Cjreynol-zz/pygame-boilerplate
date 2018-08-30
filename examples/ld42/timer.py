from pygame.font    import Font
from pygame.sprite  import Sprite


class Timer(Sprite):
    """
    Countdown timer for display on the screen.
    """

    FONT_SIZE = 30
    FONT_COLOR = (0, 0, 0)

    def __init__(self, start_time, position, background_color):
        super().__init__()

        self._time = start_time
        self.font = Font(None, self.FONT_SIZE)
        self.background_color = background_color

        self.image = self._new_image()
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value
        if self._time < 0:
            self._time = 0

    def update(self, static_groups, collectable_groups, time_delta):
        """
        Update the timer and render a new image.
        """
        self.time -= time_delta
        self.image = self._new_image()

    def _new_image(self):
        """
        Create a new surface based on the current time.
        """
        return self.font.render(self._time_string_format(self.time), 
                                    True, self.FONT_COLOR, 
                                    self.background_color)

    def _time_string_format(self, time):
        """
        Converts time in ms to MM:SS.MS format
        """
        rest, ms = divmod(time, 1000)
        mins, secs = divmod(rest, 60)
        return "{:02}:{:02}.{:03}".format(mins, secs, ms)
