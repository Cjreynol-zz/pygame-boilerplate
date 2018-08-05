from pygame.math                    import Vector2

from boilerplate.animated_sprite    import AnimatedSprite


class MovableSprite(AnimatedSprite):
    """
    Add attribute and update logic for the sprite to move around.
    """

    def __init__(self, image, size, frame_length = 0, loop = False, 
                    *groups):
        super().__init__(image, size, frame_length, loop, groups)

        self.velocity = Vector2()       # pixels per frame


    def update(self, frame_rate, collide_group):
        """
        Move the sprite a fraction of its velocity (vel / frame_rate).

        **Note** It is likely with this method that the rounding done when 
        calculating velocity (since Rects only moves by pixels, integer 
        values) that the total velocity will be wrong.  A future version 
        should correct this.
        """
        super().update()
        self.rect.topleft += self.velocity / frame_rate

    def change_velocity(self, delta_v):
        self.velocity += Vector2(delta_v)
