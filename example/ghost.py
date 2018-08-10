from os                         import path

from boilerplate.game           import Game
from boilerplate.image_loading  import load_image
from boilerplate.movable_sprite import MovableSprite


class Ghost(MovableSprite):
    """
    """

    SPRITE_PATH = path.join("example", "assets", "boo_spritesheet.png")
    SPRITE_SHEET_SIZE = (6, 1)
    ANIMATION_LENGTH = 5

    START_POS = (Game.SCREEN_SIZE[0] // 2, Game.SCREEN_SIZE[1] // 2)
    GRAVITY = (0, 0.4)
    FRICTION_VALUE = -5

    PLAYER_ACCELERATION = 1
    VELOCITY = 5
    JUMP_VELOCITY = 12
    DOWN_VELOCITY = 2

    def __init__(self):
        super().__init__(load_image(self.SPRITE_PATH), self.SPRITE_SHEET_SIZE,  
                            self.ANIMATION_LENGTH, True)

        self.position = self.START_POS
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
