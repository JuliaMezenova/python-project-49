import random


TARGET_OF_GAME = 'What is the result of the expression?'


def generate_question_and_answer():
    operand1 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])
    operand2 = random.randint(1, 100)
    question = str(operand1) + ' ' + operator + ' ' + str(operand2)
    if operator == '+':
        right_answer = operand1 + operand2
    if operator == '-':
        right_answer = operand1 - operand2
    if operator == '*':
        right_answer = operand1 * operand2
    return (question, right_answer)
