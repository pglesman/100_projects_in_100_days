from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'<b>{result}</b>'
    return wrapper


def make_emphasis(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'<em>{result}</em>'
    return wrapper


def make_underlined(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'<u>{result}</u>'
    return wrapper


@app.route("/")  # '/' means homepage
def hello_world():
    return ("<h1 style='text-align: center'>Hello, World!</h1>"
            '<p>This is paragraph.</p>'
            '<iframe src="https://giphy.com/embed/KdC9XVrVYOVu6zZiMH" width="480" height="480" frameBorder="0"'
            'class="giphy-embed" allowFullScreen></iframe>')


@app.route('/username/<name>/<int:number>')  # takes a <name> and <number> in URL as a variables
def greetings(name: str, number: int):
    return f'Hello there {name}, you are {number} years old!'


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Bye!'


if __name__ == '__main__':
    app.run(debug=True)  # activating debug mode to automate reloader
