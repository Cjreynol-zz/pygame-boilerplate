from random import choice

from collision_dir import CollisionDir
from vel_rect import VelRect


class PyPong:
    """
    The state for a game of Pong.
    """

    BALL_DIMENSIONS = (10, 10)

    PADDLE_DIMENSIONS = (10, 40)

    PADDLE_VEL = 5
    BALL_X_VEL = 3
    BALL_Y_VEL = 2
    
    def __init__(self, screen_width, screen_height):
        self.ball = None
        self.paddle1 = None
        self.paddle2 = None

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.score1 = 0
        self.score2 = 0

        self.p1_start = True
        self._initialize_objects()

    def _initialize_objects(self):
        ball_start = (self.screen_width / 2 - self.BALL_DIMENSIONS[0] / 2, 
                        self.screen_height / 2)
        self.ball = VelRect(ball_start, self.BALL_DIMENSIONS)

        paddle1_start = (self.screen_width / 8, self.screen_height / 2)
        self.paddle1 = VelRect(paddle1_start, self.PADDLE_DIMENSIONS)

        paddle2_start = (self.screen_width * 7 / 8, self.screen_height / 2)
        self.paddle2 = VelRect(paddle2_start, self.PADDLE_DIMENSIONS)

    def progress_game(self):
        self._move_ball()
        self._move_paddles()
        self._resolve_collisions()
            
    def _move_ball(self):
        self.ball.move_vel()
        if self.ball.left < 0:
            self._score(2)
        elif self.ball.right > self.screen_width:
            self._score(1)
        elif self.ball.top < 0:
            self.ball.y = 0
            self.ball.reflect_y()
        elif self.ball.bottom > self.screen_height:
            self.ball.y = self.screen_height - self.BALL_DIMENSIONS[1]
            self.ball.reflect_y()

    def _move_paddles(self):
        for paddle in [self.paddle1, self.paddle2]:
            paddle.move_vel()
            if paddle.top < 0:
                paddle.y = 0
                paddle.reflect_y()
            elif paddle.bottom > self.screen_height:
                paddle.y = self.screen_height - self.PADDLE_DIMENSIONS[1]
                paddle.reflect_y()

    def _resolve_collisions(self):
        for paddle in [self.paddle1, self.paddle2]:
            collision_dir = self.ball.collision_with(paddle)
            if collision_dir in [CollisionDir.EAST, CollisionDir.WEST]:
                self.ball.x = self.ball.last_x
                self.ball.reflect_x()
            elif collision_dir in [CollisionDir.NORTH, CollisionDir.SOUTH]:
                self.ball.y = self.ball.last_y
                self.ball.reflect_y()

    def start_ball(self):
        dy = choice([self.BALL_Y_VEL, -self.BALL_Y_VEL])
        dx = self.BALL_X_VEL
        if not self.p1_start:
            dx *= -1
        self._set_velocity(self.ball, dx, dy)

    def _reset_positions(self):
        for game_object in [self.ball, self.paddle1, self.paddle2]:
            game_object.reset()

    def _score(self, player_num):
        if player_num == 1:
            self.score1 += 1
            self.p1_start = False
        elif player_num == 2:
            self.score2 += 1
            self.p1_start = True
        
        self._reset_positions()

    def p1_up(self):
        self._set_velocity(self.paddle1, 0, -self.PADDLE_VEL)

    def p1_down(self):
        self._set_velocity(self.paddle1, 0, self.PADDLE_VEL)

    def p1_stop(self):
        self._set_velocity(self.paddle1, 0, 0)

    def p2_up(self):
        self._set_velocity(self.paddle2, 0, -self.PADDLE_VEL)

    def p2_down(self):
        self._set_velocity(self.paddle2, 0, self.PADDLE_VEL)

    def p2_stop(self):
        self._set_velocity(self.paddle2, 0, 0)
        
    def _set_velocity(self, game_obj, dx, dy):
        game_obj.dx = dx
        game_obj.dy = dy
