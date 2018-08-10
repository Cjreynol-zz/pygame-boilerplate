from boilerplate.game       import Game

from example.game_state     import GameState


def main():
    game = Game("LD 42 Testing")
    state = GameState()
    game.run(state)

if __name__ == "__main__":
    main()
