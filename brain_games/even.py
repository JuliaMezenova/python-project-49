def answer_from_user():
    import promt
    import random
    question = random.randint(1, 100)
    answer = promt.string('Question: ' + question)
    print("Your answer: " + answer)
    n = 1
    def is_right_answer(answer):
        if question%2 == 0:
            right_answer == 'yes'
        else:
            right_answer = 'no'
        return right_answer
    while n <= 3:
        if answer == right_answer:
            print('Correct!')
            n += 1
        return answer_from_user()
        else:
            print("'" + answer + "'" + "is wrong answer ;(. Correct answer was '" + right_answer + "'.")
            print("Let's try again, " + name + "!")

