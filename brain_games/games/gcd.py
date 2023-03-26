import random
from math import gcd


def start_game():
    start_game = 'Find the greatest common divisor of given numbers.'
    print(start_game)


def game_logic():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f'{num1}  {num2}'
    right_answer = gcd(num1, num2)
    return question, right_answer
