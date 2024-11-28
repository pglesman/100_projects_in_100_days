from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.snake_squares = []
        self.create_snake()
        self.head = self.snake_squares[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake_square(position)

    def add_snake_square(self, position):
        new_snake_square = Turtle(shape="square")
        new_snake_square.color("white")
        new_snake_square.up()
        new_snake_square.goto(position)
        self.snake_squares.append(new_snake_square)

    def reset(self):
        for seg in self.snake_squares:
            seg.goto(1000, 1000)
        self.snake_squares.clear()
        self.create_snake()
        self.head = self.snake_squares[0]

    def extend(self):
        self.add_snake_square(self.snake_squares[-1].position())

    def move(self):
        for i in range(len(self.snake_squares) - 1, 0, -1):
            new_x = self.snake_squares[i - 1].xcor()
            new_y = self.snake_squares[i - 1].ycor()
            self.snake_squares[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
