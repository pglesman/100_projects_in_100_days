from flask import Flask, render_template
import requests
from datetime import datetime

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


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/post/<int:blog_id>')
def read(blog_id):
    return render_template('post.html', blog_id=blog_id, posts=all_posts, today=now)


if __name__ == "__main__":
    app.run(debug=True)
