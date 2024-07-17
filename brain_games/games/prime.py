import random

from brain_games.services import is_prime

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_and_answer():
    number = random.randint(1, 100)
    question = str(number)
    answer = 'yes' if is_prime(number) else 'no'
    return question, answer
