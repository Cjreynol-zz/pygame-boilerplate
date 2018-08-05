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

def split_surface(surface, subsurface_size):
    """
    Return a list of Surface objects of the given size.

    The list will be in order from left to right, top to bottom.
    A fully-filled rectangle that is an even multiple of the size is expected.
    """
    surfaces = []
    rect = Rect((0, 0), subsurface_size)

    while rect.left < surface.get_width() and rect.top < surface.get_height():
        new_surface = surface.subsurface(rect)
        surfaces.append(new_surface)

        rect.left += rect.width
        if rect.left >= surface.get_width():
            rect.left = 0
            rect.top += rect.height

    return surfaces
