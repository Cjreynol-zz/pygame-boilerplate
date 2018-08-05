from pygame.math    import Vector2
from pygame.sprite  import Sprite

from image_loading  import split_surface


class AnimatedSprite(Sprite):
    """
    Add attributes and update logic for the sprite to cycle through images.
    """
    
    def __init__(self, sprite_sheet, size, frame_length, loop, *groups):
        """
        Initialize data used for animating the sprite.

        sprite_sheet    - sprite sheet surface, assumes the animation 
                            frames are all in a single row
        size            - width and height of a single image in the sprite_sheet
        frame_length    - number of frames per image in the animation
        loop            - boolean indicating if the animation should restart 
                            at end
        groups          - sprite groups for the sprite to join
        """
        super().__init__(groups)

        self.frame_length = frame_length
        self.loop = loop
        self.frame_count = 0

        self.images = split_surface(sprite_sheet, size)
        self.image_index = 0

        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()

    def update(self, *args):
        """
        Update the image as the game progresses
        """
        if self.frame_count >= self.frame_length:
            self.frame_count = 0

            self.image_index += 1
            if self.image_index >= len(self.images):
                if self.loop:
                    self.image_index = 0
                    self.image = self.images[self.image_index]
                else:   # keeps image_index from growing without bound
                    self.image_index -= 1
            else:
                self.image = self.images[self.image_index]

        self.frame_count += 1
