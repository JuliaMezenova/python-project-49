import random


TARGET_OF_GAME = 'What number is missing in the progression?'


def generate_question_and_answer():
    start = random.randint(1, 10)
    stop = random.randint(99, 100)
    step = random.randint(1, 10)
    first_progression = list(range(start, stop, step))
    progression = first_progression[:10]
    right_answer = random.choice(progression)
    index_of_right_answer = progression.index(right_answer)
    progression[index_of_right_answer] = '..'
    str_question = [str(num) for num in progression]
    question = " ".join(str_question)
    return (question, right_answer)
