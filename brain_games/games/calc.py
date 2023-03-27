import random


def start_game():
    start_game = 'What is the result of the expression?'
    print(start_game)


def game_logic():
    operand1 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])
    operand2 = random.randint(1, 100)
    question = str(operand1) + ' ' + operator + ' ' + str(operand2)
    right_answer = eval(question)
    return (question, right_answer)
