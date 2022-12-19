from turtle import Turtle
FONT = ("Courier", 8, "normal")


class State(Turtle):
    def __init__(self, state, x, y):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(x-10, y)
        self.write(f"{state}", True, align="left", font=FONT)
