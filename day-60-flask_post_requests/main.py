from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=["POST"])
def receive_data():
    if request.method == "POST":
        user_name = request.form['username']
        password = request.form['password']
        return f'<h1>Username: {user_name}, Password: {password}</h1>'
    return render_template("/login")


if __name__ == "__main__":
    app.run(debug=True)
