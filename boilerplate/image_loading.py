from pygame import image, Rect


def load_image(filepath):
    """
    Load the image at the path, convert it to match the display, and return 
    the resulting Surface.
    """
    loaded_image = image.load(filepath)
    if loaded_image.get_alpha() is not None:
        loaded_image = loaded_image.convert_alpha()
    else:
        loaded_image = loaded_image.convert()
    return loaded_image

def split_surface(sprite_sheet, subsurface_tuple):
    """
    Return a list of Surface objects pulled from the sprite sheet.

    The list is in order from top to bottom, left to right.
    The subsurface_tuple is expected to be (width, height).
    """
    subsurfaces = []
    surface_rect = sprite_sheet.get_rect()
    subsurface_size = (surface_rect.width // subsurface_tuple[0],
                        surface_rect.height // subsurface_tuple[1])

    rect = Rect((0, 0), subsurface_size)
    for i in range(subsurface_tuple[0]):
        rect.left = i * rect.width
        for j in range(subsurface_tuple[1]):
            rect.top = j * rect.width
            subsurfaces.append(sprite_sheet.subsurface(rect))

    return subsurfaces

def create_animation_list(filepath, subsurface_tuple):
    """
    Compose the loading and splitting of an image to create the final list 
    of animation images.
    """
    sprite_sheet = load_image(filepath)
    return split_surface(sprite_sheet, subsurface_tuple)
