from brain_games.engine import run_game
from brain_games.games import prime


def main() -> None:
    run_game(prime.DESCRIPTION, prime.get_round, prime.is_correct)


if __name__ == "__main__":
    main()
