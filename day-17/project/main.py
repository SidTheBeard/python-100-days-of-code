from question import Question
from brain import QuizBrain
from data import question_data

qs = []
playing = True
count = 0
score = 0

for question in question_data:
    qs.append(Question(question["question"], question["correct_answer"]))

b = QuizBrain(qs)


# playing = False
# playing = False


while b.still_has_questions():
    b.next_question()

print(f"Game over! Final Score: {b.score}\n\n")
