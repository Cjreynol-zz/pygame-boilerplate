from itertools import chain

from pygame import display, Surface


class GameScreen:
    """
    """

    DEFAULT_BACKGROUND_COLOR = (0, 0, 0)

    def __init__(self, window_title, screen_size):
        self.screen = self._create_screen(window_title, screen_size)
        self.background = self._create_default_background(self.screen)

    def clear(self, groups):
        for group in groups:
            group.clear(self.screen, self.background)

    def draw(self, groups):
        dirty_rect_lists = [group.draw(self.screen) for group in groups]
        return list(chain.from_iterable(dirty_rect_lists))     # flatten

    def update_display(self, dirty_rects):
        display.update(dirty_rects)

    def _create_screen(self, window_title, screen_size):
        """
        Create, configure, and return the game screen surface.
        """
        screen = display.set_mode(screen_size)
        display.set_caption(window_title)
        return screen

    def _create_default_background(self, screen):
        """
        Create background Surface, display it on the screen, and return it.
        """
        background = Surface(screen.get_size()).convert()
        background.fill(self.DEFAULT_BACKGROUND_COLOR)

        screen.blit(background, (0, 0))
        display.flip()
        return background
