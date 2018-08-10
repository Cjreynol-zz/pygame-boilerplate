from boilerplate.game       import Game

from examples.game_state     import GameState


def main():
    game = Game("Example")
    state = GameState()
    game.run(state)

if __name__ == "__main__":
    main()
