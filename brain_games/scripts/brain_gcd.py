from brain_games.engine import run_game
from brain_games.games import gcd


def main() -> None:
    run_game(gcd.DESCRIPTION, gcd.get_round, gcd.is_correct)


if __name__ == "__main__":
    main()
