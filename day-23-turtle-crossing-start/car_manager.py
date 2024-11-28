from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self, level):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setheading(180)
        self.turtlesize(stretch_len=2)
        self.setposition(280, randint(-250, 250))
        self.color(choice(COLORS))
        self.movement = STARTING_MOVE_DISTANCE + (level - 1) * MOVE_INCREMENT

    def move(self):
        self.forward(self.movement)

    def increase_movement(self):
        self.movement += MOVE_INCREMENT
