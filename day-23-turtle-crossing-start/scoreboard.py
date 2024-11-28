from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(x=-200, y=250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level} ", align="center", font=FONT)

    def increase_score(self):
        self.level += 1
        self.update_scoreboard()
