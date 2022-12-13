from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong-Game")
screen.tracer(0)

scoreboard = Scoreboard()

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


for i in range(2):
    ball = Ball()
    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        #Detect collision at top and bottom of screen
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.top_bottom_bounce()
        
        #Detect collision at paddle
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.paddle_bounce()


        #Detect collision edge of screen
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.l_point()

        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.r_point()

screen.exitonclick()