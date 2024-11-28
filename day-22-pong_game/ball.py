from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self, x_move, y_move):
        new_x = self.xcor() + x_move
        new_y = self.ycor() + y_move
        self.goto(new_x, new_y)
