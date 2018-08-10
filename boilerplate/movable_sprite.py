from itertools import chain

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

        self.jumping = False

    @property
    def position(self):
        return self.rect.topleft

    @position.setter
    def position(self, value):
        self.rect.topleft = Vector2(value)

    def update(self, static_groups, collectable_groups):
        """
        Update the sprite for a single frame of movement, then detect and 
        handle different collision types.
        """
        super().update()

        delta_d = self.velocity
        delta_v = self.acceleration

        self.position += delta_d 
        self.velocity += delta_v

        static_collisions = self._detect_collisions(static_groups)
        self._handle_collisions(static_collisions)

        collectable_collisions = self._detect_collisions(collectable_groups, 
                                                            True)
        return collectable_collisions

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
                    self.velocity += (0, -self.velocity.y)
                    self.jumping = False
                elif collision.rect.collidepoint(self.rect.midleft):
                    self.rect.left = collision.rect.right

    def _detect_collisions(self, groups, kill = False):
        """
        Determine if this Sprite intersects any of the Sprites in any of the 
        collision groups.

        ** NOTE **
        Very simple, fails to act as expected if the velocity moves this 
        Sprite all the way through the colliding sprite
        """
        collision_lists = [spritecollide(self, group, kill) 
                            for group in groups]
        return list(chain.from_iterable(collision_lists))   # flatten
