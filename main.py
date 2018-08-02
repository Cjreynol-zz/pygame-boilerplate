from os             import path
from pygame         import draw, display, event, image, init, quit, Surface

from pygame.locals  import (QUIT, KEYDOWN, KEYUP,
                            K_DOWN, K_ESCAPE, K_LEFT, K_UP, K_RIGHT)

from pygame.time    import Clock


# globals
FPS = 30
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (255, 255, 255)
TITLE = "LD42 Testing"
IMG_DIR = "img"

done = False
clock = Clock()
screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption(TITLE)

background = Surface(screen.get_size()).convert()
background.fill(BACKGROUND_COLOR)
screen.blit(background, (0, 0))
display.flip()

ghost_sprites = [image.load(path.join(IMG_DIR, "pix_boo.png"))
                    .convert_alpha(),
                    image.load(path.join(IMG_DIR, "pix_boo2.png"))
                    .convert_alpha()]
animation_index = 0
animation_speed = FPS // 2
animation_index_limit = len(ghost_sprites) * animation_speed

ghost_x, ghost_y = 10, 10
ghost_size = ghost_sprites[0].get_width(), ghost_sprites[0].get_height()
ghost_vel = 32
last_rect = None


# helpers
def handle_events(event_list):
    global ghost_x
    global ghost_y
    global done

    for event in event_list:
        if (event.type == QUIT or
            (event.type == KEYDOWN and event.key == K_ESCAPE)):
            done = True
        if event.type == KEYDOWN and event.key == K_DOWN:
            ghost_y += ghost_vel
        elif event.type == KEYDOWN and event.key == K_UP:
            ghost_y -= ghost_vel
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            ghost_x += ghost_vel
        elif event.type == KEYDOWN and event.key == K_LEFT:
            ghost_x -= ghost_vel

def clear():
    global last_rect

    ghost_pos = ghost_x, ghost_y
    last_rect = screen.blit(background, ghost_pos, ghost_pos + ghost_size)
    

def render():
    global animation_index

    animation_index += 1
    if animation_index >= animation_index_limit:
        animation_index = 0

    sprite_rect = screen.blit(ghost_sprites[animation_index 
                                                // animation_speed], 
                                (ghost_x, ghost_y))

    dirty_rects = [sprite_rect]
    if last_rect is not None:
        dirty_rects.append(last_rect)

    display.update(dirty_rects)

def main():
    while not done:
        clock.tick(FPS)
        clear()
        handle_events(event.get())
        render()

if __name__ == "__main__":
    init()
    main()
    quit()
