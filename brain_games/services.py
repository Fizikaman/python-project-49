def is_even(number):
    return number % 2 == 0


def generate_progression(start, step, length):
    return [start + i * step for i in range(length)]