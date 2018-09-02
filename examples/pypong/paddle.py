from boilerplate.movabe_sprite  import MovableSprite


class Paddle(MovableSprite):
    """
    """

    VELOCITY = 5

    def __init__(self, animation_dict, start_position):
        super().__init__(animation_dict, start_position)

    def move_down(self):
        self.velocity.y += self.VELOCITY
    
    def cancel_down(self):
        self.velocity.y += -self.VELOCITY
    
    def move_up(self):
        self.velocity.y += self.VELOCITY

    def cancel_up(self):
        self.velocity.y += -self.VELOCITY
