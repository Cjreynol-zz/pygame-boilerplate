from os                             import path

from boilerplate.animated_sprite    import AnimatedSprite
from boilerplate.animation          import Animation


class Pickup(AnimatedSprite):
    """
    Wrapper specifically used for the game's shrinking pickups.
    """

    PICKUP_PATH = path.join("examples", "ld42", "assets", "shrink_pickup.png")
    PICKUP_SHEET_SIZE = (2, 1)
    ANIMATION_FRAME_LENGTH = 15

    def __init__(self, position):
        pickup_animation = Animation(self.PICKUP_PATH, 
                                        self.PICKUP_SHEET_SIZE, 
                                        self.ANIMATION_FRAME_LENGTH, 
                                        True)
        super(). __init__(pickup_animation, position)
