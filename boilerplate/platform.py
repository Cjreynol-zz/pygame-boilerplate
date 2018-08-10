from pygame         import Surface
from pygame.sprite  import Sprite


class Platform(Sprite):
    """
    Static Sprite used as a collision object for MovableSprites.
    """

    def __init__(self, sprite, platform_size, start_pos):
        """
        Expects the image as a Surface and the platform size as a 
        (width, height) tuple of image tiles
        """
        super().__init__()

        self.image = self._create_platform(sprite, platform_size)
        self.rect = self.image.get_rect()
        self.rect.topleft = start_pos
    
    def _create_platform(self, sprite, platform_size):
        """
        Creates a new Surface for the platform and tiles the given sprite 
        over it.
        """
        rect = sprite.get_rect()
        image = Surface((rect.width * platform_size[0], 
                                rect.height * platform_size[1]))

        for i in range(platform_size[0]):
            rect.left = i * rect.width
            for j in range(platform_size[1]):
                rect.top = j * rect.height
                image.blit(sprite, rect)

        return image
