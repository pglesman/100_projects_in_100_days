from flask import Flask, render_template
import random
from datetime import datetime
import requests

agify_url = 'https://api.agify.io'
genderize_url = 'https://api.genderize.io'
blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(0, 99)
    current_year = datetime.now().year
    return render_template('index.html', num=random_number, year=current_year)


@app.route('/guess/<some_name>')
def guess_age_gender(some_name: str):
    param = {
        'name': some_name,
    }
    name = some_name.title()
    agify_response = requests.get(agify_url, params=param)
    agify_json = agify_response.json()
    age = agify_json['age']

    genderize_response = requests.get(genderize_url, params=param)
    genderize_json = genderize_response.json()
    gender = genderize_json['gender']

    return render_template('guess.html', name=name, age=age, gender=gender)


@app.route('/blog/<num>')  # 'num' variable is taken from 'url_for' hyperlink in index.html
def get_blog(num):
    print(num)
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
