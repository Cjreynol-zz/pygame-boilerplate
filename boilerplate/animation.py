from pygame.transform           import scale

from boilerplate.image_loading  import create_animation_list


class Animation:
    """
    Stores the information needed to display and animation on the screen.
    """

    def __init__(self, path, sheet_size = (1, 1), frame_length = 1, 
                    loop = False):
        self.animation_list = create_animation_list(path, sheet_size)
        self.frame_length = frame_length
        self.loop = loop

    def scale(self, scale_factor):
        """
        Convert the animation's images based on the given scale_factor.
        """
        rect = self.animation_list[0].get_rect()
        new_width, new_height = (int(rect.width * scale_factor), 
                                int(rect.height * scale_factor))

        return [scale(image, (new_width, new_height)) 
                    for image in self.animation_list]
