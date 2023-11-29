from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.label = Label(text="Score:", bg=THEME_COLOR, fg='white')
        self.label.grid(column=1, row=0)

        self.canvas_card = Canvas(width=300, height=250)
        self.question = self.canvas_card.create_text(
            150,
            125,
            width=280,
            text="Question",
            font=("Arial", 16, "italic"),
            fill=THEME_COLOR)
        self.canvas_card.grid(column=0, row=1, columnspan=2, pady=50)

        correct_img = PhotoImage(file="images/true.png")
        self.button_correct = Button(image=correct_img, highlightthickness=0, command=self.button_correct_click)
        self.button_correct.grid(column=0, row=2)
        wrong_img = PhotoImage(file="images/false.png")
        self.button_wrong = Button(image=wrong_img, highlightthickness=0, command=self.button_wrong_click)
        self.button_wrong.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas_card.config(bg='white')
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas_card.itemconfig(self.question, text=question_text)
        else:
            self.canvas_card.itemconfig(self.question, text="You have reached to the end of quiz.")
            self.button_correct.config(state='disabled')
            self.button_wrong.config(state='disabled')

    def button_correct_click(self):
        self.feedback(self.quiz.check_answer("True"))

    def button_wrong_click(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_right):
        if is_right:
            self.canvas_card.config(bg='#A5EC6A')
        else:
            self.canvas_card.config(bg='#E7396E')
        self.window.after(1000, self.get_next_question)
