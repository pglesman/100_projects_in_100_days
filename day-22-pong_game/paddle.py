from turtle import Turtle

MOVEMENT = 20


class Paddle(Turtle):

    def __init__(self, x_pos: int):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setposition(x_pos, 0)
        self.setheading(90)
        self.turtlesize(stretch_len=5)
        self.color("white")

    def up(self):
        self.forward(MOVEMENT)

    def down(self):
        self.backward(MOVEMENT)
