from boilerplate.image_loading  import create_animation_list


class Animation:
    """
    """

    def __init__(self, path, sheet_size = (1, 1), frame_length = 1, 
                    loop = False):
        self.animation_list = create_animation_list(path, sheet_size)
        self.frame_length = frame_length
        self.loop = loop
