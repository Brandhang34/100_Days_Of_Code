from turtle import Turtle, Screen
import random


screen = Screen()

race_ongoing = False

screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle=[]


y_pos = -100
for turtle_index in range (0,6):
	new_turtle = Turtle(shape="turtle")
	new_turtle.color(colors[turtle_index])
	new_turtle.penup()
	new_turtle.goto(x=-230, y=y_pos)
	all_turtle.append(new_turtle)
	y_pos+=40

if user_bet:
	race_ongoing = True

while(race_ongoing):
	for turtle in all_turtle:
		random_distance = random.randint(0,10)
		turtle.forward(random_distance)
		if turtle.xcor() >= 250:
			race_ongoing = False
			winning_color = turtle.pencolor()
			if winning_color == user_bet:
				print(f"you've won! The {winning_color} turtle is the winner!")
			else:
				print(f"your {user_bet} turtle lost.")


screen.exitonclick()
