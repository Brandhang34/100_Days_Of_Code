from tkinter import *
from quiz_brain import *


THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz=quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")

        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)

        self.canvas.grid(row=1, column=0, columnspan=2)
        

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1, padx=20, pady=20)


        self.question = self.canvas.create_text(150, 125, text="Word", font=("Arial", 10, "italic"), fill=THEME_COLOR, width=250)

        self.true_button_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_button_image, command=self.true_answer)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)

        self.false_button_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_button_image, command=self.false_answer)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()


        self.window.mainloop()
    
    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=q_text)
        self.canvas.config(bg="white")


    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))
        self.score_label.config(text=f"Score: {self.quiz.score}")
    def false_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))
        self.score_label.config(text=f"Score: {self.quiz.score}")
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)