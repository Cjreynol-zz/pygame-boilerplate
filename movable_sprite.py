from animator       import Animator

from pygame.math    import Vector2
from pygame.sprite  import Sprite


class MovableSprite(Sprite):
    """
    Adds the attributes and update method logic for moving the sprite on the 
    screen.
    """

    def __init__(self, image, size, frame_length = 0, loop = False, 
                    *groups):
        super().__init__(groups)

        self.animator = Animator(image, size, frame_length, loop)
        self.image = self.animator.get_image()
        self.rect = self.image.get_rect()

        self.velocity = Vector2()       # distance, expected per second value


    def update(self, frame_rate):
        """
        Move the sprite a fraction of its velocity (vel / frame_rate).

        **Note** It is likely with this method that the rounding done when 
        calculating velocity (since Rects only moves by pixels, integer 
        values) that the total velocity will be wrong.  A future version 
        should correct this.
        """
        self.rect.topleft += self.velocity / frame_rate

        new_image = self.animator.update()
        if new_image is not None:
            self.image = new_image

    def change_velocity(self, delta_v):
        """
        """
        self.velocity += Vector2(delta_v)
