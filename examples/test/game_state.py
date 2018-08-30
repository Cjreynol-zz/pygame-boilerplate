from os                                 import path

from pygame.locals                      import (QUIT, K_DOWN, K_ESCAPE, 
                                                K_LEFT, K_UP, K_RIGHT, 
                                                KEYDOWN, KEYUP)
from pygame.sprite                      import RenderUpdates

from boilerplate.animation              import Animation
from boilerplate.animation_state        import AnimationState
from boilerplate.animated_sprite        import AnimatedSprite
from boilerplate.image_loading          import load_image
from boilerplate.game                   import Game
from boilerplate.game_state_abc         import GameStateABC
from boilerplate.platform               import Platform
from boilerplate.platformer_character   import PlatformerCharacter


class GameState(GameStateABC):
    """
    """
    
    IMG_DIR = path.join("examples", "test", "assets")
    GHOST_PATH = path.join(IMG_DIR, "boo_spritesheet.png")
    GHOST_SHEET_SIZE = (6, 1)

    WALL_PATH = path.join(IMG_DIR, "wood_panel_tile.png")
    PICKUP_PATH = path.join(IMG_DIR, "pickup_sheet.png")
    PICKUP_SHEET_SIZE = (2, 1)

    def __init__(self):
        super().__init__()

        self.ghost = self._create_ghost()
        self.ghost_group = RenderUpdates(self.ghost)

        walls = self._create_walls()
        self.wall_group = RenderUpdates(*walls)

        pickups = self._create_pickups()
        self.pickup_group = RenderUpdates(*pickups)

    def _create_ghost(self):
        ghost_animations = {AnimationState.IDLE : 
                                Animation(self.GHOST_PATH, 
                                            self.GHOST_SHEET_SIZE, 5, True)}
                                    
        return PlatformerCharacter(ghost_animations, (400, 200))

    def _create_walls(self):
        wall_tile = load_image(self.WALL_PATH)
    
        bottom = Platform(wall_tile, 
                            (Game.SCREEN_SIZE[0] // Game.SQUARE_SIZE[0], 1),
                            (0, Game.SCREEN_SIZE[1] - Game.SQUARE_SIZE[1]))
        left = Platform(wall_tile, 
                            (1, Game.SCREEN_SIZE[1] // Game.SQUARE_SIZE[1]),
                            (0, 0))
        right = Platform(wall_tile, 
                            (1, Game.SCREEN_SIZE[1] // Game.SQUARE_SIZE[1]),
                            (Game.SCREEN_SIZE[0] - Game.SQUARE_SIZE[0], 0))

        platform_size = (5, 1)
        platform1 = Platform(wall_tile, platform_size, 
                                (Game.SCREEN_SIZE[0] // 2 
                                    - Game.SQUARE_SIZE[0], 
                                Game.SCREEN_SIZE[1] * 5 / 6))
        platform2 = Platform(wall_tile, platform_size,
                                (Game.SCREEN_SIZE[0] // 2 
                                    - Game.SQUARE_SIZE[0] * 4,
                                Game.SCREEN_SIZE[1] * 3 / 5))

        return [bottom, left, right, platform1, platform2]

    def _create_pickups(self):
        pickup_animation = Animation(self.PICKUP_PATH, self.PICKUP_SHEET_SIZE, 
                                        15, True)

        pickup1 = AnimatedSprite(pickup_animation, 
                                    (Game.SCREEN_SIZE[0] // 2 
                                        - Game.SQUARE_SIZE[0], 
                                    Game.SCREEN_SIZE[1] * 5 / 6 
                                        - Game.SQUARE_SIZE[1]))

        pickup2 = AnimatedSprite(pickup_animation,
                                    (Game.SCREEN_SIZE[0] // 2 
                                        - Game.SQUARE_SIZE[0] * 4,
                                    Game.SCREEN_SIZE[1] * 3 / 5 
                                        - Game.SQUARE_SIZE[1]))
        return [pickup1, pickup2]

    def get_all_groups(self):
        return [self.ghost_group, self.wall_group, self.pickup_group]

    def get_static_groups(self):
        return [self.wall_group]

    def get_collectable_groups(self):
        return [self.pickup_group]

    def handle_events(self, event_list):
        for event in event_list:
            if (event.type == QUIT or
                (event.type == KEYDOWN and event.key == K_ESCAPE)):
                self.done = True

            if event.type == KEYDOWN and event.key == K_DOWN:
                self.ghost.move_down()
            elif event.type == KEYUP and event.key == K_DOWN:
                self.ghost.cancel_down()

            elif event.type == KEYDOWN and event.key == K_UP:
                self.ghost.jump()
                
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                self.ghost.move_right()
            elif event.type == KEYUP and event.key == K_RIGHT:
                self.ghost.cancel_right()

            elif event.type == KEYDOWN and event.key == K_LEFT:
                self.ghost.move_left()
            elif event.type == KEYUP and event.key == K_LEFT:
                self.ghost.cancel_left()
