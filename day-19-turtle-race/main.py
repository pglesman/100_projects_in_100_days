from random import randint
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle win the race, enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = {}
y = 150
is_race_on = True

for color in colors:
    turtles[color] = Turtle(shape="turtle")
    turtle = turtles[color]
    turtle.color(color)
    turtle.up()
    turtle.goto(x=-230, y=y)
    y -= 60

while is_race_on:
    for turtle_name, turtle in turtles.items():
        turtle.forward(randint(0, 10))
        if turtle.xcor() > 230:
            if user_bet == turtle_name:
                print(f"You've won! {turtle_name.title()} turtle is the winner")
            else:
                print(f"You've lost. {turtle_name.title()} turtle has won.")
            is_race_on = False
            break

screen.exitonclick()
