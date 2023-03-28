import random


def start_game():
    start_game = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    print(start_game)


def game_logic():
    question = random.randint(2, 200)
    counter = 0
    for divisor in range(2, question // 2 + 1):
        if (question % divisor == 0):
            counter += 1
    if counter <= 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return (question, right_answer)
