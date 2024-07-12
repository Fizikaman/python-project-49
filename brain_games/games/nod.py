import random
import math

RULES = ("Суть игры в следующем: вам показывается два случайных числа, например, 25 50.\n"
         "Вы должны вычислить и ввести наибольший общий делитель этих чисел.")


def generate_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    answer = str(math.gcd(num1, num2))
    return question, answer
