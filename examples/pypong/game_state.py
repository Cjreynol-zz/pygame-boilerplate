from os                         import path

from pygame.locals              import (QUIT, KEYDOWN, KEYUP, K_DOWN, 
                                        K_ESCAPE, K_s, K_SPACE, K_UP, K_w)
from pygame.sprite              import RenderUpdates

from boilerplate.game           import Game
from boilerplate.game_state_abc import GameStateABC
from boilerplate.image_loading      import load_image
from boilerplate.platform           import Platform

from examples.pypong.paddle     import Paddle
from examples.pypong.ball       import Ball


class GameState(GameStateABC):
    """
    """

    BORDER_PATH = path.join("examples", "pypong", "assets", 
                            "pypong_square.png")

    def __init__(self):
        super().__init__()

        self.ball = self._create_ball()
        self.ball_group = RenderUpdates(self.ball)

        self.paddles = self._create_paddles()
        self.paddle_group = RenderUpdates(*self.paddles)

        self.border_walls = self._create_border()
        self.border_group = RenderUpdates(*self.border_walls)

    def get_all_groups(self):
        return [self.ball_group, self.paddle_group, self.border_group]

    def get_static_groups(self):
        return [self.border_group]

    def get_collectable_groups(self):
        return []

    def _create_ball(self):
        ball_start = (Game.SCREEN_SIZE[0] / 2, Game.SCREEN_SIZE[1] / 2)
        return Ball(ball_start)

    def _create_paddles(self):
        paddle1_start = (Game.SCREEN_SIZE[0] / 8, Game.SCREEN_SIZE[1] / 2)
        paddle1 = Paddle(paddle1_start)

        paddle2_start = (Game.SCREEN_SIZE[0] * 7 / 8, Game.SCREEN_SIZE[1] / 2)
        paddle2 = Paddle(paddle2_start)

        return (paddle1, paddle2)

    def _create_border(self):
        border_image = load_image(self.BORDER_PATH)
        horizontal_size = (50, 1)
        vertical_size = (1, 40)
        square_size = 16

        top = Platform(border_image, horizontal_size, (0, -square_size / 2))
        right = Platform(border_image, vertical_size, 
                            (Game.SCREEN_SIZE[0] - square_size / 2, 0))
        bottom = Platform(border_image, horizontal_size, 
                            (0, Game.SCREEN_SIZE[1] - square_size / 2))
        left = Platform(border_image, vertical_size, (-square_size / 2, 0))
        
        return (top, right, bottom, left)

    def handle_events(self, event_list):
        for event in event_list:
            if (event.type == QUIT or 
                        (event.type == KEYDOWN and event.key == K_ESCAPE)):
                self.done = True

            if event.type == KEYDOWN and event.key == K_SPACE:
                self.ball.start()

            if event.type == KEYDOWN and event.key == K_w:
                self.paddles[0].move_up()
            elif event.type == KEYUP and event.key == K_w:
                self.paddles[0].cancel_up()
            if event.type == KEYDOWN and event.key == K_s:
                self.paddles[0].move_down()
            elif event.type == KEYUP and event.key == K_s:
                self.paddles[0].cancel_down()

            if event.type == KEYDOWN and event.key == K_UP:
                self.paddles[1].move_up()
            elif event.type == KEYUP and event.key == K_UP:
                self.paddles[1].cancel_up()
            if event.type == KEYDOWN and event.key == K_DOWN:
                self.paddles[1].move_down()
            elif event.type == KEYUP and event.key == K_DOWN:
                self.paddles[1].cancel_down()
