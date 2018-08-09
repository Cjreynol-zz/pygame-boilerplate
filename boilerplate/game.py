from pygame                     import event, init, quit
from pygame.time                import Clock

from boilerplate.game_screen    import GameScreen


class Game:
    """
    The manager class for controlling the game screen and running the game 
    state.
    """
    
    SCREEN_SIZE = (800, 640)
    FPS = 30

    def __init__(self, title):
        self.screen = GameScreen(title, self.SCREEN_SIZE)
        self.clock = Clock()
        
    def run(self, state):
        """
        Play the game until it reaches a final state. 
        """
        init()

        while not state.done:
            self.clock.tick(self.FPS)
            self.screen.clear(state.get_all_groups())
            state.handle_events(event.get())

            state.update()
            dirty_rects = self.screen.draw(state.get_all_groups())
            self.screen.update_display(dirty_rects)

        quit()
