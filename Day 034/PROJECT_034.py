from question_model import Question
from quiz_brain import QuizBrain
import requests
from ui import QuizInterface


OPEN_TRIVIA_URL = "https://opentdb.com/api.php?amount=10&type=boolean"


def get_questions():
    response = requests.get(url=OPEN_TRIVIA_URL)
    response.raise_for_status()
    questions = response.json()
    return questions["results"]


question_data = get_questions()
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)
ui = QuizInterface(quiz_brain)


