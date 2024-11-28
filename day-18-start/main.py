from turtle import Turtle, Screen
from random import randint

tim = Turtle()
tim.shape("arrow")
tim.color("red")

screen = Screen()
screen.colormode(255)  # set screen to RGB model

angles = [0, 90, 180, 270]


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def draw_spirograph(size_of_gap: int):
    for angle in range(0, 360 + size_of_gap, size_of_gap):
        tim.circle(100)
        tim.color(random_color())
        tim.setheading(angle)


tim.speed("fastest")

draw_spirograph(5)

screen.exitonclick()
