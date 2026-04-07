import random

MIN_NUMBER = 1
MAX_NUMBER = 100
PARITY_DIVISOR = 2

DESCRIPTION = (
    'Answer "yes" if the number is even, otherwise answer "no".'
)


def get_round() -> tuple[str, str]:
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct = "yes" if number % PARITY_DIVISOR == 0 else "no"
    return str(number), correct


GAME = (DESCRIPTION, get_round)
