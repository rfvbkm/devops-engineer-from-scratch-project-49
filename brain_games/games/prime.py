import random

MIN_NUMBER = 1
MAX_NUMBER = 100

SMALLEST_PRIME = 2
FIRST_ODD_DIVISOR = 3
DIVISOR_STEP = 2

DESCRIPTION = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
)


def is_prime(n: int) -> bool:
    if n < SMALLEST_PRIME:
        return False
    if n == SMALLEST_PRIME:
        return True
    if n % SMALLEST_PRIME == 0:
        return False
    divisor = FIRST_ODD_DIVISOR
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += DIVISOR_STEP
    return True


def get_round() -> tuple[str, str]:
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct = "yes" if is_prime(number) else "no"
    return str(number), correct


def is_correct(answer: str, correct: str) -> bool:
    return answer in ("yes", "no") and answer == correct
