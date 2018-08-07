from pygame.math                    import Vector2
from pygame.sprite                  import spritecollide

from boilerplate.animated_sprite    import AnimatedSprite


class MovableSprite(AnimatedSprite):
    """
    Add attribute and update logic for the sprite to move around.
    """

    def __init__(self, image, size, frame_length = 0, loop = False, 
                    *groups):
        super().__init__(image, size, frame_length, loop, groups)

        self.velocity = Vector2()       # pixels per frame
        self.acceleration = Vector2()

    def update(self, frame_rate, collide_group):
        """
        Move the sprite a fraction of its velocity (vel / frame_rate).

        ** NOTE ** 
        It is likely with this method that the rounding done when calculating 
        velocity (since Rects only moves by pixels, integer values) that the 
        total velocity will be wrong.  A future version should correct this.
        """
        super().update()

        delta_d = self.velocity / frame_rate
        delta_v = self.acceleration / frame_rate

        self.change_position(delta_d)
        self.change_velocity(delta_v)

        collisions = self._detect_collisions(collide_group)
        self._handle_collisions(collisions)

    def _handle_collisions(self, collisions):
        """
        Set proper position after collisions, make other state adjustments.
        """
        if collisions:
            for collision in collisions:
                if collision.rect.collidepoint(self.rect.midtop):
                    self.rect.top = collision.rect.bottom
                elif collision.rect.collidepoint(self.rect.midright):
                    self.rect.right = collision.rect.left
                elif collision.rect.collidepoint(self.rect.midbottom):
                    self.rect.bottom = collision.rect.top
                    self.change_velocity((0, -self.velocity.y))
                elif collision.rect.collidepoint(self.rect.midleft):
                    self.rect.left = collision.rect.right

    def _detect_collisions(self, collide_group):
        """
        Determine if this Sprite intersects any of the Sprites in the other 
        group.

        ** NOTE **
        Very simple, fails to act as expected if the velocity moves this 
        Sprite through the colliding sprite
        """
        return spritecollide(self, collide_group, False)

    def change_velocity(self, delta_v):
        self.velocity += Vector2(delta_v)

    def change_acceleration(self, delta_a):
        self.acceleration += Vector2(delta_a)

    def change_position(self, delta_d):
        self.rect.topleft += Vector2(delta_d)
