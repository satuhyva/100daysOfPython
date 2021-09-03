import random

class Quizzer:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.keep_playing = True

    @staticmethod
    def input_is_ok(input_text):
        if input_text != "t" and input_text != "f":
            print("Answer must be t or f!")
            return False
        return True

    @staticmethod
    def check_answer(correct, guessed):
        print(f"The correct answer was: {correct}.")
        correct_answer = ("f", "t")[correct == "True"]
        if correct_answer == guessed:
            print("You got it right!")
            return True
        else:
            print("Wrong answer!")
            return False

    def next_question(self):
        next_number = random.randint(0, len(self.question_list) - 1)
        question = self.question_list.pop(next_number)
        print(len(self.question_list))
        guess = input(
            f"\nQ.{self.question_number + 1}: {question.text} True (t) or false (f)? ")
        if not self.input_is_ok(guess):
            return
        correct_answer = question.answer
        answer_is_correct = self.check_answer(correct_answer, guess)
        if answer_is_correct:
            self.score += 1
        print(f"Your current score is {self.score}/{self.question_number + 1}.")
        self.question_number += 1
        go_again = input("Go again (y or n)? ")
        if not go_again == 'y':
            self.keep_playing = False

    def still_has_questions(self):
        if len(self.question_list) > 0:
            return True
        return False

    def print_final_result(self):
        print(f"\nYour final score is: {self.score}/{self.question_number}.")
