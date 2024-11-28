import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = [CarManager(scoreboard.level)]

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if randint(0, 100) > 90:
        car_manager.append(CarManager(scoreboard.level))

    for car in car_manager:
        if player.distance(car) < 25:
            game_is_on = False
            break

    if player.ycor() > 220:
        scoreboard.increase_score()
        player.restart()
        for car in car_manager:
            car.increase_movement()

    for car in car_manager:
        car.move()
        if car.xcor() > 300:
            car_manager.remove(car)

screen.exitonclick()
