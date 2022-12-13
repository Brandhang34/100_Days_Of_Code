import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
screen.listen()
screen.onkey(turtle.up, "Up")
car_manager=CarManager()

scoreboard = Scoreboard()

game_is_on = True
generate_car_counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move()
    if generate_car_counter == 5:
        car_manager.create_cars()
        generate_car_counter =0
    else:
        generate_car_counter += 1
    
    for car in car_manager.all_cars:
        if turtle.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if turtle.ycor() > 280:
        turtle.reset()
        car_manager.increase_speed()
        scoreboard.add_1()
    
screen.exitonclick()
