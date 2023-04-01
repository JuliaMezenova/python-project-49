import random


TARGET_OF_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_and_answer():
    question = random.randint(2, 200)

    def is_prime_num(question):
        counter = 0
        for divisor in range(2, question // 2 + 1):
            if (question % divisor == 0):
                counter += 1
        if counter <= 0:
            return True
        else:
            return False
    if is_prime_num(question):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return (question, right_answer)
