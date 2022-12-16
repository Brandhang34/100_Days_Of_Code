from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,xcor, ycor):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(xcor, ycor)
        self.score = 0

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
    
    def add_score(self):
        self.score += 1