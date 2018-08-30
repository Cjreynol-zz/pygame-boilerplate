from pygame.font    import Font
from pygame.sprite  import Sprite


class TotalTime(Sprite):
    """
    """

    FONT_SIZE = 30
    FONT_COLOR = (0, 0, 0)

    def __init__(self, position, background_color):
        super().__init__()
        
        self.time = 0
        self.font = Font(None, self.FONT_SIZE)
        self.background_color = background_color

        self.image = self._new_image()
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self, static_groups, collectable_groups, time_delta):
        """
        """
        self.time += time_delta
        self.image = self._new_image()

    def _new_image(self):
        """
        """
        return self.font.render(self._time_string_format(self.time),
                                True, self.FONT_COLOR,
                                self.background_color)

    def _time_string_format(self, time):
        """
        """
        mins, secs = divmod(time // 1000, 60)
        return "{:02}:{:02}".format(mins, secs)
