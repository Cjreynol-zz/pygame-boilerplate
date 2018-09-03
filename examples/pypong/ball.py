from os                             import path
from random                         import choice

from boilerplate.animation          import Animation
from boilerplate.animation_state    import AnimationState
from boilerplate.movable_sprite     import MovableSprite


class Ball(MovableSprite):
    """
    """

    BALL_PATH = path.join("examples", "pypong", "assets", 
                            "pypong_square.png")
    IDLE_SIZE = (1, 1)
    IDLE_FRAME_LENGTH = 100       # is it better to have this long or short?

    VELOCITY = 4

    def __init__(self, start_position):
        animation_dict = { AnimationState.IDLE : 
                            Animation(self.BALL_PATH,
                                        self.IDLE_SIZE,
                                        self.IDLE_FRAME_LENGTH) }
        super().__init__(animation_dict, start_position)

        self.start_position = start_position

    def _handle_collisions(self, collisions):
        for collision in collisions:
            if collision.rect.collidepoint(self.rect.midtop):
                self.reflect_y()
            elif collision.rect.collidepoint(self.rect.midright):
                self.reflect_x()
            elif collision.rect.collidepoint(self.rect.midbottom):
                self.reflect_y()
            elif collision.rect.collidepoint(self.rect.midleft):
                self.reflect_x()
        super()._handle_collisions(collisions)

    def reset_pos(self):
        self.position = self.start_position

    def start(self):
        self.velocity.y = choice([self.VELOCITY, -self.VELOCITY])
        self.velocity.x = choice([self.VELOCITY, -self.VELOCITY])

    def reflect_x(self):
        self.velocity.x *= -1

    def reflect_y(self):
        self.velocity.y *= -1
