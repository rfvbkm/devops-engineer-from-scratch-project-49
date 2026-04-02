import random

from brain_games.engine import Game

MIN_NUMBER = 1
MAX_NUMBER = 100

DESCRIPTION = (
    'Answer "yes" if the number is even, otherwise answer "no".'
)


def get_round() -> tuple[str, str]:
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct = "yes" if number % 2 == 0 else "no"
    return str(number), correct


def is_correct(answer: str, correct: str) -> bool:
    return answer in ("yes", "no") and answer == correct


GAME = Game(
    description=DESCRIPTION,
    get_round=get_round,
    is_correct=is_correct,
)
