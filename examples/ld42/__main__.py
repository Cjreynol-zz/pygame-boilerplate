from boilerplate.game           import Game

from examples.ld42.game_state   import GameState


def main():
    game = Game("Example")
    state = GameState()
    game.full_screen_run(state)

if __name__ == "__main__":
    main()
