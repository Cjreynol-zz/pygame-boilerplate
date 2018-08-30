from boilerplate.game           import Game

from examples.test.game_state   import GameState


def main():
    game = Game("Example")
    state = GameState()
    game.dirty_rect_run(state)

if __name__ == "__main__":
    main()
