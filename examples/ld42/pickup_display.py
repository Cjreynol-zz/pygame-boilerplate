from pygame.font    import Font
from pygame.sprite  import Sprite


class PickupDisplay(Sprite):
    """
    """

    FONT_SIZE = 30
    FONT_COLOR = (0, 0, 0)

    def __init__(self, position, background_color):
        super().__init__()

        self.font = Font(None, self.FONT_SIZE)
        self.background_color = background_color

        self.image = self._new_image(0)
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update_display(self, count):
        self.image = self._new_image(count)
        
    def _new_image(self, count):
        return self.font.render(self._display_string(count), 
                                    True, self.FONT_COLOR, 
                                    self.background_color)

    def _display_string(self, count):
        return "Pickup Count - {}/3".format(count)
