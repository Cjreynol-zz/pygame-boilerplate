from os             import path
from pygame         import draw, display, event, image, init, quit

from pygame.locals  import QUIT, KEYDOWN, KEYUP
from pygame.locals  import K_DOWN, K_ESCAPE, K_LEFT, K_UP, K_RIGHT

from pygame.time    import Clock


# globals
FPS = 30
SCREEN_SIZE = 1024

done = False
clock = Clock()
screen = display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
display.set_caption("LD42 Testing")

ghost_sprite = image.load(path.join("img", "pix_boo.png"))
ghost_x, ghost_y = 10, 10
ghost_vel = 10


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


def render():
    screen.fill((255, 255, 255))
    screen.blit(ghost_sprite, (ghost_x, ghost_y))
    display.flip()

def main():
    while not done:
        clock.tick(FPS)
        handle_events(event.get())
        render()

if __name__ == "__main__":
    init()
    main()
    quit()
