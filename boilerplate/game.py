from pygame                     import event, init, quit

from boilerplate.game_screen    import GameScreen
from boilerplate.game_state     import GameState


class Game:
    """
    """
    
    TITLE = "LD42 Testing"
    SCREEN_SIZE = (800, 640)

    def __init__(self):
        self.screen = GameScreen(self.TITLE, self.SCREEN_SIZE)
        self.state = GameState()
        
    def run(self):
        """
        Run the main logic loop of the game.
        """
        init()

        while not self.state.done:
            self.state.tick()
            self.screen.clear(self.state.get_groups())
            self.state.handle_events(event.get())

            self.state.update()
            dirty_rects = self.screen.draw(self.state.get_groups())
            self.screen.update_display(dirty_rects)

        quit()
