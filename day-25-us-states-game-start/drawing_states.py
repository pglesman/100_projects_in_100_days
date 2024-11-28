from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 10, "normal")


class DrawingStates(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")

    def draw(self, state, x_cor, y_cor):
        self.goto(x_cor, y_cor)
        self.write(f"{state}", align=ALIGNMENT, font=FONT)