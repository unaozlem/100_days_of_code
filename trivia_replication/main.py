from question_model import Question
from trivia_data import question_data
from quiz_brain import QuizBrain

# TODO: asking the question
# TODO: checking the answer was correct
# TODO: checking if we are the end of the quiz


question_bank = []

for question in question_data:
    text = question["question"]
    answer = question["correct_answer"]
    question_item = Question(text, answer)
    question_bank.append(question_item)

    
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the game.")
print(f"Your final score is {quiz.score}/{quiz.question_number}.")

