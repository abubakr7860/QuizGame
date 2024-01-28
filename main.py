from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for question in question_data:
    question_text = question["text"]
    question_answer = question["correct_answer"]
    next_question = Question(question_text,question_answer)
    question_bank.append(next_question)


quiz=QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("you have completed: ")
print(f"your final score: {quiz.score}/{quiz.question_number}")