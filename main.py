from pygame             import event, init, quit

from game_screen        import GameScreen
from game_state         import GameState


def main():
    screen = GameScreen()
    game = GameState()

    while not game.done:
        game.tick()
        screen.clear(game.ghost_group)
        game.handle_events(event.get())

        game.update()
        dirty_rects = screen.draw(game.ghost_group)
        screen.update_display(dirty_rects)

if __name__ == "__main__":
    init()

    main()

    quit()
