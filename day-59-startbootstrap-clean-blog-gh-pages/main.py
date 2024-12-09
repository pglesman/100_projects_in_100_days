import os
import smtplib
from datetime import datetime

import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request

# Load environment variables from .env file
load_dotenv()

MY_EMAIL = os.environ["MY_EMAIL"]
PASSWORD = os.environ["PASSWORD"]
YAHOO_EMAIL = os.environ["YAHOO_EMAIL"]

# Creating json file for blog posts
npoint_api_url = 'https://api.npoint.io/41ab157af71948072505'  # https://www.npoint.io/

app = Flask(__name__)

response = requests.get(npoint_api_url)
all_posts = response.json()
now = datetime.now()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts, today=now)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        email_message = f'Name: {name}, email: {email}, phone: {phone}, message: {message}'
        print(email_message)

        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=YAHOO_EMAIL,
                msg=f'Subject:New user {name}\n\n{email_message}'
            )
            print('Mail send!')

        return render_template('contact.html', msg_sent=True)
    else:
        return render_template("contact.html", msg_sent=False)


@app.route('/post/<int:blog_id>')
def read(blog_id):
    return render_template('post.html', blog_id=blog_id, posts=all_posts, today=now)


if __name__ == "__main__":
    app.run(debug=True)
