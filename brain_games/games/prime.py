import random

from brain_games.services import is_prime

RULES = ("Суть игры в следующем: вам показывается "
         "случайное число, например, 25.\n"
         "Вы должны - 'Yes', если число простое, "
         "в противном случае ответ 'No'.")


def generate_question_and_answer():
    number = random.randint(1, 100)
    question = str(number)
    answer = 'yes' if is_prime(number) else 'no'
    return question, answer
