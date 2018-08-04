from os                 import path

from pygame             import draw, display, event, image, init, quit, Surface
from pygame.locals      import (QUIT, KEYDOWN, KEYUP,
                                K_DOWN, K_ESCAPE, K_LEFT, K_UP, K_RIGHT)
from pygame.math        import Vector2
from pygame.sprite      import RenderUpdates
from pygame.time        import Clock

from movable_sprite    import MovableSprite


FPS = 30
SCREEN_WIDTH = 800      # 32 * 25
SCREEN_HEIGHT = 640     # 32 * 20
BACKGROUND_COLOR = (25, 25, 255)
TITLE = "LD42 Testing"
IMG_DIR = "imgs"

GHOST_SPRITE_SHEET = "boo_spritesheet.png"
SPRITE_SIZE = (32, 32)
FRAME_LENGTH = FPS // 6
VELOCITY = 128

done = False
clock = Clock()
screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption(TITLE)

background = Surface(screen.get_size()).convert()
background.fill(BACKGROUND_COLOR)
screen.blit(background, (0, 0))
display.flip()

def load_image(filename):
    full_path = path.join(IMG_DIR, filename)
    sprite = image.load(full_path)
    if sprite.get_alpha() is not None:
        sprite = sprite.convert_alpha()
    else:
        sprite = sprite.convert()
    return sprite

def handle_events(event_list):
    global done
    global ghost

    for event in event_list:
        if (event.type == QUIT or
            (event.type == KEYDOWN and event.key == K_ESCAPE)):
            done = True

        if event.type == KEYDOWN and event.key == K_DOWN:
            ghost.velocity += Vector2(0, VELOCITY)
        elif event.type == KEYUP and event.key == K_DOWN:
            ghost.velocity -= Vector2(0, VELOCITY)

        elif event.type == KEYDOWN and event.key == K_UP:
            ghost.velocity += Vector2(0, -VELOCITY)
        elif event.type == KEYUP and event.key == K_UP:
            ghost.velocity -= Vector2(0, -VELOCITY)
            
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            ghost.velocity += Vector2(VELOCITY, 0)
        elif event.type == KEYUP and event.key == K_RIGHT:
            ghost.velocity -= Vector2(VELOCITY, 0)

        elif event.type == KEYDOWN and event.key == K_LEFT:
            ghost.velocity += Vector2(-VELOCITY, 0)
        elif event.type == KEYUP and event.key == K_LEFT:
            ghost.velocity -= Vector2(-VELOCITY, 0)

sheet = load_image(GHOST_SPRITE_SHEET)
ghost = MovableSprite(sheet, SPRITE_SIZE, FRAME_LENGTH, True)
group = RenderUpdates(ghost)

def main():
    while not done:
        clock.tick(FPS)
        group.clear(screen, background)
        handle_events(event.get())

        group.update(FPS)
        dirty_rects = group.draw(screen)
        display.update(dirty_rects)

if __name__ == "__main__":
    init()
    main()
    quit()
