from os             import path

from pygame.locals  import (QUIT, KEYDOWN, KEYUP,
                                K_DOWN, K_ESCAPE, K_LEFT, K_UP, K_RIGHT)
from pygame.sprite  import RenderUpdates
from pygame.time    import Clock

from image_loading  import load_image
from movable_sprite import MovableSprite


class GameState:
    
    FPS = 30

    ANIMATION_FRAMES = 5

    VELOCITY = 128

    def __init__(self):
        self.ghost = self._create_ghost()
        self.ghost_group = RenderUpdates(self.ghost)
        self.clock = Clock()

        self.done = False

    def _create_ghost(self):
        ghost_path = path.join("imgs", "boo_spritesheet.png")

        sheet = load_image(ghost_path)
        ghost = MovableSprite(sheet, (32, 32), self.ANIMATION_FRAMES, True)
        return ghost

    def tick(self):
        return self.clock.tick(self.FPS)

    def update(self):
        self.ghost_group.update(self.FPS)

    def handle_events(self, event_list):
        for event in event_list:
            if (event.type == QUIT or
                (event.type == KEYDOWN and event.key == K_ESCAPE)):
                self.done = True

            if event.type == KEYDOWN and event.key == K_DOWN:
                self.ghost.change_velocity((0, self.VELOCITY))
            elif event.type == KEYUP and event.key == K_DOWN:
                self.ghost.change_velocity((0, -self.VELOCITY))

            elif event.type == KEYDOWN and event.key == K_UP:
                self.ghost.change_velocity((0, -self.VELOCITY))
            elif event.type == KEYUP and event.key == K_UP:
                self.ghost.change_velocity((0, self.VELOCITY))
                
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                self.ghost.change_velocity((self.VELOCITY, 0))
            elif event.type == KEYUP and event.key == K_RIGHT:
                self.ghost.change_velocity((-self.VELOCITY, 0))

            elif event.type == KEYDOWN and event.key == K_LEFT:
                self.ghost.change_velocity((-self.VELOCITY, 0))
            elif event.type == KEYUP and event.key == K_LEFT:
                self.ghost.change_velocity((self.VELOCITY, 0))

