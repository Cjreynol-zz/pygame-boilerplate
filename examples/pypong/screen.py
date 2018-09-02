from pygame import display, draw

from pygame.font import Font


class Screen:
    """
    The screen manager for a game of Pong.
    """

    WINDOW_TITLE = "PyPong"

    SCREEN_WIDTH = 450
    SCREEN_HEIGHT = 300
    FONT_SIZE = 50

    BACKGROUND_COLOR = (0, 0, 0)
    BACKGROUND_EFFECTS_COLOR = (255, 255, 255)
    OBJECT_COLOR = (0, 255, 20)

    MIDLINE_START = (SCREEN_WIDTH / 2, 0)
    MIDLINE_STOP = (SCREEN_WIDTH / 2, SCREEN_HEIGHT)
    SCORE1_POS = (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 6)
    SCORE2_POS = (SCREEN_WIDTH * 3 / 4, SCREEN_HEIGHT / 6)

    def __init__(self):
        self.screen = self._initialize_window()
        self.font = Font(None, self.FONT_SIZE)

    def _initialize_window(self):
        screen = display.set_mode(self.screen_dimensions())
        display.set_caption(self.WINDOW_TITLE)
        return screen

    def screen_dimensions(self):
        return self.SCREEN_WIDTH, self.SCREEN_HEIGHT

    def render_screen(self, game):
        self._render_background(game.score1, game.score2)
        for game_object in [game.ball, game.paddle1, game.paddle2]:
            draw.rect(self.screen, self.OBJECT_COLOR, game_object)
        display.flip()

    def _render_background(self, score1, score2):
        self.screen.fill(self.BACKGROUND_COLOR)
        draw.line(self.screen, self.BACKGROUND_EFFECTS_COLOR,
                    self.MIDLINE_START, self.MIDLINE_STOP)

        score1_text = self.font.render(str(score1), True, 
                                        self.BACKGROUND_EFFECTS_COLOR)
        score2_text = self.font.render(str(score2), True, 
                                        self.BACKGROUND_EFFECTS_COLOR)
        self.screen.blit(score1_text, self.SCORE1_POS)
        self.screen.blit(score2_text, self.SCORE2_POS)
