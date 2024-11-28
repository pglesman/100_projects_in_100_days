from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(x=0, y=270)
        self.pencolor("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Left paddle: {self.l_score} | Right paddle: {self.r_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self, x_pos):
        if x_pos > 380:
            self.l_score += 1
        elif x_pos < -380:
            self.r_score += 1

        self.update_scoreboard()