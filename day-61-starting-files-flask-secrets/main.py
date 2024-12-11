import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]

bootstrap = Bootstrap5(app)

admin_credentials = ['admin@email.com', '12345678']


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        user_email = login_form.email.data
        password_email = login_form.password.data
        if [user_email, password_email] == admin_credentials:
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
