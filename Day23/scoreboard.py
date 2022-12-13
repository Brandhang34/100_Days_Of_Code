from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-280,250)
        self.write(f"Score: {self.level}", True, align="left", font=FONT)

    def add_1(self):
        self.level += 1
        self.clear()
        self.color("black")
        self.penup()
        self.goto(-280,250)
        self.hideturtle()
        self.write(f"Score: {self.level}", True, align="left", font=FONT)

    def game_over(self):
        self.goto(-80,0)
        self.write("Game Over", True, align="left", font=FONT)