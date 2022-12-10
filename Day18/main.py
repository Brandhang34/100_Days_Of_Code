import turtle as t
from turtle import Screen
import random

timmy_the_turtle = t.Turtle()
timmy_the_turtle.color("red")
timmy_the_turtle.speed("fastest")
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color
# sides = 3
# for i in range(0,8):
#     angle = 360 / sides
#     for j in range(sides):
#         timmy_the_turtle.fd(50)
#         timmy_the_turtle.right(angle)
#     sides +=1

# def right():
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.right(90)
#     timmy_the_turtle.fd(50)
# def left():
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.left(90)
#     timmy_the_turtle.fd(50)
# def forward():
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.fd(50)
# def back():
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.right(180)
#     timmy_the_turtle.fd(50)

# for i in range (200):
#     direction = random.randint(1,4)
#     if direction == 1:
#         right()
#     elif direction == 2:
#         left()
#     elif direction == 3:
#         forward()
#     elif direction == 4:
#         back()
for i in range (0, 100):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.circle(100)
    timmy_the_turtle.left(5)

screen = Screen()
screen.exitonclick()
