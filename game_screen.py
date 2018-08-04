from pygame         import display, Surface


class GameScreen:
    """
    """

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 640

    TITLE = "LD42 Testing"
    BACKGROUND_COLOR = (0, 0, 0)

    def __init__(self):
        self.screen = self._create_screen()
        self.background = self._create_background(self.screen)

    def clear(self, group):
        group.clear(self.screen, self.background)

    def draw(self, group):
        return group.draw(self.screen)

    def update_display(self, dirty_rects):
        display.update(dirty_rects)

    def _create_screen(self):
        """
        Create, configure, and return the game screen surface.
        """
        screen = display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        display.set_caption(self.TITLE)
        return screen

    def _create_background(self, screen):
        """
        Create background Surface, display it on the screen, and return it.
        """
        background = Surface(screen.get_size()).convert()
        background.fill(self.BACKGROUND_COLOR)

        screen.blit(background, (0, 0))
        display.flip()
        return background
