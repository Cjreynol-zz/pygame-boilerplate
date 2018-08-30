from pygame                     import event, init, quit
from pygame.time                import Clock

from boilerplate.game_screen    import GameScreen


class Game:
    """
    The manager class for controlling the game screen and running the game 
    state.
    """
    
    SCREEN_SIZE = (800, 640)
    SQUARE_SIZE = (32, 32)
    FPS = 30

    def __init__(self, title):
        init()
        self.screen = GameScreen(title, self.SCREEN_SIZE)
        self.clock = Clock()

    def run(self, state):
        self.dirty_rect_run(state)
        
    def dirty_rect_run(self, state):
        """
        Play the game until it reaches a final state. 
        """
        while not state.done:
            time_delta = self.clock.tick(self.FPS)
            self.screen.clear(state.get_all_groups())
            state.handle_events(event.get())

            state.update(time_delta)
            dirty_rects = self.screen.draw(state.get_all_groups())
            self.screen.update_display(dirty_rects)

        quit()

    def full_screen_run(self, state):
        """
        Play the game until it reaches a final state. 
        """
        while not state.done:
            time_delta = self.clock.tick(self.FPS)
            state.handle_events(event.get())

            state.update(time_delta)

            self.screen.draw_all(state.get_all_groups(), 
                                    state.player.velocity)
            self.screen.update()

        quit()
