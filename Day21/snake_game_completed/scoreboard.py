from turtle import Turtle
from food import Food


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        #self.write("score: ", True, align='center', font=('Arial', 8, 'normal'))
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.write(f"Score: {self.score}", True, align='center', font=('Arial', 20, 'normal'))
    
    def add_1(self):
        self.score += 1
        self.clear()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.write(f"Score: {self.score}", True, align='center', font=('Arial', 20, 'normal'))
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", True, align='center', font=('Arial',20, "normal"))