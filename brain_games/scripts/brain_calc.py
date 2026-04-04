from brain_games.engine import run_game
from brain_games.games import calc


def main() -> None:
    run_game(calc.DESCRIPTION, calc.get_round, calc.is_correct)


if __name__ == "__main__":
    main()
