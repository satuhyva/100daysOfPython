# different kind of importing
import question
# from data import question_data as questions_list    # alias name in import
from open_trivia_questions import data as questions_list
from quizzer import Quizzer

question_bank = []
for item in questions_list:
    question_bank.append(question.Question(item["question"], item["correct_answer"]))
    # question_bank.append(question.Question(item["text"], item["answer"]))

quizzer = Quizzer(question_bank)
while quizzer.still_has_questions() and quizzer.keep_playing:
    quizzer.next_question()
quizzer.print_final_result()


# https://opentdb.com/api_config.php


