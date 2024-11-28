import colorgram
import turtle as t
from random import choice

colors = colorgram.extract("image.jpg", 30)

for i, color in enumerate(colors):
    colors[i] = (colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b)

colors = colors[5:]  # slice off colors that are close to background color, colors are in listed sorted by frequency
# print(colors)

tim = t.Turtle()
x = -440
y = -440
tim.speed("fastest")
t.colormode(255)
tim.hideturtle()

for i in range(10):
    for j in range(10):
        tim.teleport(x + j * 90, y + i * 90)
        tim.color(choice(colors))
        tim.begin_fill()
        tim.circle(20)
        tim.end_fill()

screen = t.Screen()
screen.exitonclick()
