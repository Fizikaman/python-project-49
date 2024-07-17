import random

from brain_games.services import is_prime

RULES = 'What number is missing in the progression?'


def generate_question_and_answer():
    number = random.randint(1, 100)
    question = str(number)
    answer = 'yes' if is_prime(number) else 'no'
    return question, answer
