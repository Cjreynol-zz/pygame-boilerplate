from os                             import path

from boilerplate.animation          import Animation
from boilerplate.animation_state    import AnimationState
from boilerplate.movable_sprite     import MovableSprite


class Paddle(MovableSprite):
    """
    """

    PADDLE_PATH = path.join("examples", "pypong", "assets", 
                            "paddle.png")
    IDLE_SIZE = (1, 1)
    IDLE_FRAME_LENGTH = 100       # is it better to have this long or short?

    VELOCITY = 5

    def __init__(self, start_position):
        animation_dict = { AnimationState.IDLE : 
                            Animation(self.PADDLE_PATH,
                                        self.IDLE_SIZE,
                                        self.IDLE_FRAME_LENGTH) }
        super().__init__(animation_dict, start_position)

        self.start_position = start_position

    def reset_pos(self):
        self.position = self.start_position

    def move_down(self):
        self.velocity.y += self.VELOCITY
    
    def cancel_down(self):
        self.velocity.y += -self.VELOCITY
    
    def move_up(self):
        self.velocity.y += -self.VELOCITY

    def cancel_up(self):
        self.velocity.y += self.VELOCITY
