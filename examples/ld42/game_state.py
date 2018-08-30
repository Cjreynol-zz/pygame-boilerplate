from os                             import path

from pygame.locals                  import (QUIT, KEYDOWN, KEYUP, 
                                            K_DOWN, K_LEFT, K_RIGHT, K_UP, 
                                            K_ESCAPE, 
                                            K_SPACE, K_o, K_p)
from pygame.sprite                  import RenderUpdates

from boilerplate.game               import Game
from boilerplate.game_state_abc     import GameStateABC
from boilerplate.image_loading      import load_image
from boilerplate.platform           import Platform

from examples.ld42.pickup           import Pickup
from examples.ld42.pickup_display   import PickupDisplay
from examples.ld42.player           import Player
from examples.ld42.timer            import Timer
from examples.ld42.total_time       import TotalTime


class GameState(GameStateABC):
    """
    The current plan is to have a character move around in a labyrinth-style 
    world with a timer counting down.  When the timer hits 0 the character grows, 
    potentially ending the game if they are stuck in a space that is too small to 
    hold their new size.  

    The maze the character navigates will be different sizes, sometimes with 
    shortcuts to travel through if the character is small enough.  To aid the 
    character there will be pickups that can be activated to shrink down to their 
    last size.
    """

    SCALE_FACTOR = 1.8
    PLAYER_START = (Game.SCREEN_SIZE[0] // 2, Game.SCREEN_SIZE[1] // 2)

    TIMER_POSITION = (Game.SCREEN_SIZE[0] * 3 / 4, 0)
    START_TIME = 30 * 1000  # 30 seconds

    TOTAL_TIME_POSITION = (Game.SCREEN_SIZE[0] * 2 / 4, 0)
    PICKUP_COUNT_POSITION = (0, 0)

    PICKUP_START = (Game.SCREEN_SIZE[0] // 2, Game.SCREEN_SIZE[1] * 3 / 4)

    PLATFORM_SIZE = (5, 1)
    PLATFORM1_POSITION = (Game.SCREEN_SIZE[0] * 1 / 4, 
                            Game.SCREEN_SIZE[1] * 1 / 4)
    PLATFORM2_POSITION = (Game.SCREEN_SIZE[0] * 1 / 4, 
                            Game.SCREEN_SIZE[1] * 2 / 4)

    def __init__(self):
        super().__init__()

        self.player = self._make_player()
        self.player_group = RenderUpdates(self.player)

        self.pickup_count = self._make_pickup_count()
        self.total_time = self._make_total_time()
        self.timer = self._make_timer()
        self.display_group = RenderUpdates(self.timer, self.total_time, 
                                            self.pickup_count)

        self.pickup = self._make_pickup()
        self.pickup_group = RenderUpdates(self.pickup)

        self.walls = self._make_walls()
        self.walls_group = RenderUpdates(*self.walls)

    def _make_player(self):
        return Player(self.PLAYER_START)

    def _make_timer(self):
        return Timer(self.START_TIME, self.TIMER_POSITION, (255, 255, 255))

    def _make_total_time(self):
        return TotalTime(self.TOTAL_TIME_POSITION, (255, 255, 255))

    def _make_pickup_count(self):
        return PickupDisplay(self.PICKUP_COUNT_POSITION, (255, 255, 255))

    def _make_pickup(self):
        return Pickup(self.PICKUP_START)

    def _make_walls(self):
        platform_tile = load_image(path.join("examples", "ld42", "assets", "wall_tile.png"))
        return [Platform(platform_tile, self.PLATFORM_SIZE, 
                            self.PLATFORM1_POSITION), 
                Platform(platform_tile, self.PLATFORM_SIZE,
                            self.PLATFORM2_POSITION)]

    def update(self, time_delta):
        """
        Trigger events based on the timer.
        """
        super().update(time_delta)

        self.pickup_count.update_display(self.player.pickup_count)

        if self.timer.time == 0:
            self.player.scale(self.SCALE_FACTOR)
            self.timer.time = self.START_TIME

    def get_all_groups(self):
        return [self.player_group, self.display_group, self.pickup_group, 
                    self.walls_group]

    def get_static_groups(self):
        return [self.walls_group]

    def get_collectable_groups(self):
        return [self.pickup_group]

    def handle_events(self, event_list):
        for event in event_list:
            if (event.type == QUIT or
                (event.type == KEYDOWN and event.key == K_ESCAPE)):
                self.done = True

            elif event.type == KEYDOWN and event.key == K_DOWN:
                self.player.move_down()
            elif event.type == KEYUP and event.key == K_DOWN:
                self.player.cancel_down()

            elif event.type == KEYDOWN and event.key == K_UP:
                self.player.move_up()
            elif event.type == KEYUP and event.key == K_UP:
                self.player.cancel_up()
                
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                self.player.move_right()
            elif event.type == KEYUP and event.key == K_RIGHT:
                self.player.cancel_right()

            elif event.type == KEYDOWN and event.key == K_LEFT:
                self.player.move_left()
            elif event.type == KEYUP and event.key == K_LEFT:
                self.player.cancel_left()

            elif (event.type == KEYUP and event.key == K_SPACE
                    and self.player.pickup_count > 0):
                self.player.pickup_count -= 1
                self.player.scale(1.0 / self.SCALE_FACTOR)

            # debug
            elif event.type == KEYDOWN and event.key == K_p:
                self.player.scale(self.SCALE_FACTOR)
            elif event.type == KEYDOWN and event.key == K_o:
                self.player.scale(1.0 / self.SCALE_FACTOR)
