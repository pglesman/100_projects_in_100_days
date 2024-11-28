import turtle
import pandas as pd
from drawing_states import DrawingStates

IMAGE = "blank_states_img.gif"

data = pd.read_csv("50_states.csv")
states = pd.DataFrame(data)

draw_states = DrawingStates()

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)
score = 0
states.set_index("state", inplace=True)

while True:
    answer_state = (screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")).title()

    if states["x"].get(answer_state):
        x_cor = states["x"].get(answer_state)
        y_cor = states["y"].get(answer_state)
        score += 1
        draw_states.draw(answer_state, x_cor, y_cor)

    if score == 50:
        break

screen.exitonclick()
