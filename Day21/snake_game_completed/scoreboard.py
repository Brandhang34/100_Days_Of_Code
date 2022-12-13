from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.write("score: ", True, align='left', font=('Arial', 8, 'normal'))
