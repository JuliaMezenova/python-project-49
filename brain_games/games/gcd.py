import random


TARGET_OF_GAME = 'Find the greatest common divisor of given numbers.'


def generate_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f'{num1} {num2}'

    def gcd(num1, num2):
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 %= num2
            else:
                num2 %= num1
        return num1 or num2
    right_answer = gcd(num1, num2)
    return (question, right_answer)
