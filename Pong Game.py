from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detects Collision with Up and Down Walls.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detects Collision with Paddle.
    if ball.distance(r_paddle) < 30 and ball.xcor() > 330 or ball.distance(l_paddle) < 30 and ball.xcor() < -330:
        ball.bounce_x()

    #Detects when right paddle misses.
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detects when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()