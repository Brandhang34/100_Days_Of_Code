# import colorgram
import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
tim.speed("fastest")
tim.hideturtle()
t.colormode(255)

# pallete_colors = colorgram.extract('image.jpg',30)

# colors = []
# for i in range (len(pallete_colors)):
#     rgb = pallete_colors[i].rgb
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b
#     colors.append((r,g,b))

# print(colors)

color_list = [(132, 166, 204), (220, 148, 108), (197, 135, 148), (32, 41, 61), (163, 59, 49), (41, 106, 155), (141, 183, 162), 
(237, 211, 92), (148, 61, 68), (214, 83, 72), (35, 61, 56), (52, 111, 91), (170, 29, 33), (158, 33, 30), (234, 167, 158), (17, 97, 71), (52, 44, 48), (230, 161, 165), (171, 188, 220), (58, 52, 49), (184, 103, 113), (32, 60, 108), (107, 127, 159), (175, 200, 188), (35, 150, 209), (66, 66, 56)]
tim.penup()
tim.goto(-300,-300)
print(tim.pos())

for i in range (10):
    for j in range (10):
        tim.forward(50)
        tim.dot(20, random.choice(color_list))
    tim.left(90)
    tim.forward(50)
    tim.right(90)
    tim.setx(-300)


screen = Screen()
screen.exitonclick()