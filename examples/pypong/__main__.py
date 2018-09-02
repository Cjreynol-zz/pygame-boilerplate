from boilerplate.game           import Game
from examples.pypong.game_state import GameState


def main():
    game = Game("PyPong")
    state = GameState()
    game.dirty_rect_run(state)

if __name__ == "__main__":
    main()
