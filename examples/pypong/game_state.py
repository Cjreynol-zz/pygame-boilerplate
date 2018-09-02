from pygame.locals              import (QUIT, KEYDOWN, KEYUP, K_DOWN, 
                                        K_ESCAPE, K_s, K_SPACE, K_UP, K_w)
from pygame.sprite              import RenderUpdates

from boilerplate.game_state_abc import GameStateABC


class GameState(GameStateABC):
    """
    """

    FPS = 30

    def __init__(self):
        super().__init__()

        self.ball = self._create_ball()
        self.ball_group = RenderUpdates(self.ball)

        self.paddles = self._create_paddles()
        self.paddle_group = RenderUpdates(*self.paddles)

        self.border_walls = self._create_border()
        self.border_group = RenderUpdates(*self.border_walls)

    def get_all_groups(self):
        return [self.ball_group, self.paddle_group]

    def get_static_groups(self):
        return []

    def get_collectable_groups(self):
        return []

    def _create_ball(self):
        ball_start = (self.screen_width / 2 - self.BALL_DIMENSIONS[0] / 2, 
                        self.screen_height / 2)
        return VelRect(ball_start, self.BALL_DIMENSIONS)

    def _create_paddles(self):
        paddle1_start = (self.screen_width / 8, self.screen_height / 2)
        paddle1 = VelRect(paddle1_start, self.PADDLE_DIMENSIONS)

        paddle2_start = (self.screen_width * 7 / 8, self.screen_height / 2)
        paddle2 = VelRect(paddle2_start, self.PADDLE_DIMENSIONS)

        return (paddle1, paddle2)

    def _create_border(self):
        pass

    def handle_events(self, event_list):
        for event in event_list:
            if (event.type == QUIT or 
                        (event.type == KEYDOWN and event.key == K_ESCAPE)):
                self.done = True

            if event.type == KEYDOWN and event.key == K_SPACE:
                self.game.start_ball()

            if event.type == KEYDOWN and event.key == K_w:
                self.game.p1_up()
            if event.type == KEYDOWN and event.key == K_s:
                self.game.p1_down()
            if event.type == KEYUP and (event.key == K_w or event.key == K_s):
                self.game.p1_stop()

            if event.type == KEYDOWN and event.key == K_UP:
                self.game.p2_up()
            if event.type == KEYDOWN and event.key == K_DOWN:
                self.game.p2_down()
            if event.type == KEYUP and (event.key == K_UP or event.key == K_DOWN):
                self.game.p2_stop()
