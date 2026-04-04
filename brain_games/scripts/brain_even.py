from brain_games.engine import run_game
from brain_games.games import even


def main() -> None:
    run_game(even.DESCRIPTION, even.get_round, even.is_correct)


if __name__ == "__main__":
    main()
