from flask import Flask

app = Flask(__name__)


@app.route("/")  # '/' means homepage
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/username/<name>/<int:number>')  # takes a <name> and <number> in URL as a variables
def greetings(name: str, number: int):
    return f'Hello there {name}, you are {number} years old!'


if __name__ == '__main__':
    app.run(debug=True)  # activating debug mode to automate reloader
