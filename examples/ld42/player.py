from os                             import path

from boilerplate.animation          import Animation
from boilerplate.animation_state    import AnimationState
from boilerplate.movable_sprite     import MovableSprite


class Player(MovableSprite):
    """
    Keeps track of the state of the player character and has convenience 
    functions for key presses.
    """

    PLAYER_IDLE_PATH = path.join("examples", "ld42", "assets", "running_guy.png")
    IDLE_SIZE = (2, 1)
    IDLE_FRAME_LENGTH = 4
    VELOCITY = 5
    
    PICKUP_MAX = 3

    def __init__(self, start_position):
        animation_dict = {
                            AnimationState.IDLE : 
                                Animation(self.PLAYER_IDLE_PATH, 
                                            self.IDLE_SIZE, 
                                            self.IDLE_FRAME_LENGTH, 
                                            True)
                            }
        super().__init__(animation_dict, start_position)

        self.last_move = 0
        self._pickup_count = 0

    @property
    def pickup_count(self):
        return self._pickup_count

    @pickup_count.setter
    def pickup_count(self, value):
        self._pickup_count = value
        if self._pickup_count > self.PICKUP_MAX:
            self._pickup_count = self.PICKUP_MAX

    def _handle_collectables(self, collected):
        if collected:
            self.pickup_count += len(collected)

    def update(self, *args):
        self.last_move = super().update(*args)
        
    # event helper functions
    def scale(self, scale_factor):
        current_center = self.rect.center
        self.scale_animation(scale_factor)
        self.rect.center = current_center
        
    def move_right(self):
        self.velocity.x += self.VELOCITY

    def cancel_right(self):
        self.velocity.x += -self.VELOCITY

    def move_left(self):
        self.velocity.x += -self.VELOCITY

    def cancel_left(self):
        self.velocity.x += self.VELOCITY

    def move_up(self):
        self.velocity.y += -self.VELOCITY

    def cancel_up(self):
        self.velocity.y += self.VELOCITY

    def move_down(self):
        self.velocity.y += self.VELOCITY

    def cancel_down(self):
        self.velocity.y += -self.VELOCITY
