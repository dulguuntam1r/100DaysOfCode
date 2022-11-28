from quiz_data import question_data
from quiz_question_model import QuestionModel
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_text = item["question"]
    question_answer = item["answer"]
    new_question = QuestionModel(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Congratz. You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")