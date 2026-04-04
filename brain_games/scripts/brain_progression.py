from brain_games.engine import run_game
from brain_games.games import progression


def main() -> None:
    run_game(
        progression.DESCRIPTION,
        progression.get_round,
        progression.is_correct,
    )


if __name__ == "__main__":
    main()
