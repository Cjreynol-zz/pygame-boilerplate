from itertools      import chain

from pygame         import display, Surface
from pygame.math    import Vector2

#from examples.ld42.pickup_display import PickupDisplay
#from examples.ld42.timer          import Timer
#from examples.ld42.total_time     import TotalTime


class GameScreen:
    """
    """

    DEFAULT_BACKGROUND_COLOR = (0, 0, 0)
    WHITE = (255, 255, 255)

    def __init__(self, window_title, screen_size):
        self.screen_size = screen_size
        self.screen = self._create_screen(window_title, self.screen_size)

        self.border_background, self.border_position = self._create_border(self.screen)
        self.background = self._create_default_background(self.screen)

        self.camera_offset = Vector2(0, 0)

    def clear(self, groups):
        for group in groups:
            group.clear(self.screen, self.background)

    def draw(self, groups):
        dirty_rect_lists = [group.draw(self.screen) for group in groups]
        return list(chain.from_iterable(dirty_rect_lists))     # flatten

    def draw_all(self, groups, player_move):
        self.camera_offset += player_move
        self.screen.blit(self.border_background, self.border_position)
        self.screen.blit(self.background, -self.camera_offset, 
                            ((0, 0), self.screen_size))

        for group in groups:
            for sprite in group.sprites():
                position = sprite.rect.topleft - self.camera_offset
                #if isinstance(sprite, (Timer, TotalTime, PickupDisplay)):
                #    position = sprite.rect.topleft

                self.screen.blit(sprite.image, position)

    def update_display(self, dirty_rects):
        display.update(dirty_rects)

    def update(self):
        display.flip()

    def _create_screen(self, window_title, screen_size):
        """
        Create, configure, and return the game screen surface.
        """
        screen = display.set_mode(screen_size)
        display.set_caption(window_title)
        return screen

    def _create_border(self, screen):
        """
        """
        screen_size = screen.get_size()
        border_size = (screen_size[0] * 2, screen_size[1] * 2)

        border_background = Surface(border_size).convert()
        border_background.fill(self.DEFAULT_BACKGROUND_COLOR)

        border_position = (-screen_size[0] // 2, -screen_size[1] // 2)
        screen.blit(border_background, border_position)
        display.flip()

        return border_background, border_position

    def _create_default_background(self, screen):
        """
        Create background Surface, display it on the screen, and return it.
        """
        background = Surface(screen.get_size()).convert()
        background.fill(self.WHITE)

        screen.blit(background, (0, 0))
        display.flip()
        return background
