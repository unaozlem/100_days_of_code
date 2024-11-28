from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=50, pady=50)
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            text = "Text", 
            font=("Ariel", 20, "italic"), 
            fill=THEME_COLOR,
            width=280)

        # self.false_image = PhotoImage(file = "/images/false.png")
        # self.true_image= PhotoImage(file = "/images/true.png")

        self.false_image = PhotoImage(file="/Users/ozlemunal/Desktop/100_days_coding/day_34/quizzler_app/images/false.png")
        self.true_image = PhotoImage(file="/Users/ozlemunal/Desktop/100_days_coding/day_34/quizzler_app/images/true.png")
        
        self.button_false = Button(image=self.false_image, highlightthickness=0, command=self.false_passed)
        self.button_false.grid(column=0, row=2)

        
        self.button_true = Button(image=self.true_image, highlightthickness=0, command=self.true_pressed)
        self.button_true.grid(column=1, row=2)

        self.label_score = Label(text=f"Score = 0", bg=THEME_COLOR, fg="white")
        self.label_score.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label_score.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_passed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
