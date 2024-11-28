import time
from turtle import Screen

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

X_MOV = 10
Y_MOV = 10
SLEEPING = 0.08

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(SLEEPING)

    # detect collision with upper/lower wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        Y_MOV *= -1

    # detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        X_MOV *= -1
        SLEEPING *= 0.9

    # detect paddle misses
    if ball.xcor() > 380 or ball.xcor() < -380:
        scoreboard.increase_score(ball.xcor())
        ball.home()
        screen.update()
        time.sleep(1)
        X_MOV *= -1
        SLEEPING = 0.08

    ball.move(X_MOV, Y_MOV)

screen.exitonclick()
