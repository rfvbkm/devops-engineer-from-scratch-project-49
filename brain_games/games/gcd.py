import math
import random

from brain_games.engine import Game

MIN_NUMBER = 1
MAX_NUMBER = 100

DESCRIPTION = "Find the greatest common divisor of given numbers."


def get_round() -> tuple[str, str]:
    a = random.randint(MIN_NUMBER, MAX_NUMBER)
    b = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f"{a} {b}"
    correct = str(math.gcd(a, b))
    return question, correct


def is_correct(answer: str, correct: str) -> bool:
    return answer == correct


GAME = Game(
    description=DESCRIPTION,
    get_round=get_round,
    is_correct=is_correct,
)
