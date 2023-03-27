import random
import sympy


def start_game():
    start_game = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    print(start_game)


def game_logic():
    question = random.randint(1, 200)
    if sympy.isprime(question):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return (question, right_answer)
