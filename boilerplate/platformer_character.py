from boilerplate.movable_sprite     import MovableSprite


class PlatformerCharacter(MovableSprite):
    """
    """

    GRAVITY = (0, 0.4)
    VELOCITY = 5
    JUMP_VELOCITY = 11
    DOWN_VELOCITY = 2

    def __init__(self, animation_dict, start_position):
        super().__init__(animation_dict, start_position)

        self.acceleration += self.GRAVITY

    def jump(self):
        if not self.jumping:
            self.velocity.y += -self.JUMP_VELOCITY
            self.jumping = True

    def move_right(self):
        self.velocity.x += self.VELOCITY

    def cancel_right(self):
        self.velocity.x += -self.VELOCITY

    def move_left(self):
        self.velocity.x += -self.VELOCITY

    def cancel_left(self):
        self.velocity.x += self.VELOCITY

    def move_down(self):
        if self.jumping:
            self.velocity.y += self.DOWN_VELOCITY

    def cancel_down(self):
        if self.jumping:
            self.velocity.y += -self.DOWN_VELOCITY
