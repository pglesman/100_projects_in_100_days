from flask import Flask
from random import randint

app = Flask(__name__)

random_number = randint(0, 9)


def too_low_decorator(func):
    def wrapper(number):
        result = func(number)
        if number < random_number:
            return (f"<h1 style='color:red'>Too low, try again!</h1>"
                    '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
                    f'{result}')
        else:
            return result
    return wrapper


def too_high_decorator(func):
    def wrapper(number):
        result = func(number)
        if number > random_number:
            return (f"<h1 style='color:blue'>Too high, try again!</h1>"
                    '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
                    f'{result}')
        else:
            return result
    return wrapper


def correct_decorator(func):
    def wrapper(number):
        result = func(number)
        if number == random_number:
            return (f"<h1 style='color:green'>You found me!</h1>"
                    '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
                    f'{result}')
        else:
            return result
    return wrapper


@app.route("/")  # '/' means homepage
def guess_the_number():
    return ("<h1 style='text-align: center'>Guess a number between 0 and 9!</h1>"
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')


@app.route("/<int:number>")
@too_low_decorator
@too_high_decorator
@correct_decorator
def generated_url(number):
    return f''


if __name__ == '__main__':
    app.run(debug=True)  # activating debug mode to automate reloader
