from pygame.math                import Vector2
from pygame.sprite              import Sprite


class AnimatedSprite(Sprite):
    """
    Add attributes and update logic for the sprite to cycle through images.
    """
    
    def __init__(self, animation, position):
        super().__init__()

        self.reset(animation, position)

    def reset(self, animation, position):
        self.frame_length = animation.frame_length
        self.loop = animation.loop
        self.frame_count = 0

        self.images = animation.animation_list
        self.image_index = 0

        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.topleft = position

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
