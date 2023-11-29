from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []
for question in question_data:
    newQ = Question(question["question"], question["correct_answer"])
    question_bank.append(newQ)
quiz = Quizbrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print(f"You've completed the quiz.\nYour final score is {quiz.score}/{quiz.question_number}")
