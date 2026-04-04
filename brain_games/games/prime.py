import random

from brain_games.engine import Game

MIN_NUMBER = 1
MAX_NUMBER = 100

DESCRIPTION = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def get_round() -> tuple[str, str]:
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct = "yes" if is_prime(number) else "no"
    return str(number), correct


def is_correct(answer: str, correct: str) -> bool:
    return answer in ("yes", "no") and answer == correct


GAME = Game(
    description=DESCRIPTION,
    get_round=get_round,
    is_correct=is_correct,
)
