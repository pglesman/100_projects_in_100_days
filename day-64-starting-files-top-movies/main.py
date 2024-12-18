from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length
import requests
from dotenv import load_dotenv
import os

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

API_TOKEN_MOVIE_DB = os.environ['API_TOKEN_MOVIE_DB']
URL_MOVIE_DB = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"

headers_movie_db = {
    "accept": "application/json",
    'Authorization': f'Bearer {API_TOKEN_MOVIE_DB}',
}

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-movies-collection.db"
# initialize the app with the extension
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=True)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=True)

    def __repr__(self):
        return f'<Movie {self.title}>'


class RateMovieForm(FlaskForm):
    rating = FloatField('Your Rating Out of 10 e.g. 7.5 ', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired(), Length(5, 50)])
    submit = SubmitField('Done')


class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired(), Length(2, 30)])
    submit = SubmitField('Add Movie')


with app.app_context():
    db.create_all()


def get_movie_list(title: str) -> list:
    movie_db_params = {
        'query': title,
    }
    try:
        response = requests.get(URL_MOVIE_DB, headers=headers_movie_db, params=movie_db_params)
        movie_list: list = response.json()['results']
    except requests.exceptions.RequestException as err:
        print(f"Exception request: {err}")
        movie_list = []
    return movie_list


def get_movie_details(movie_db_id: int) -> dict:
    movie_url = f"https://api.themoviedb.org/3/movie/{movie_db_id}?language=en-US"
    try:
        response = requests.get(movie_url, headers=headers_movie_db)
        movie_details = response.json()
    except requests.exceptions.RequestException as err:
        print(f"Exception request: {err}")
        movie_details = {}
    return movie_details


def add_movie(movie_details: dict) -> str:
    title = movie_details['original_title']
    img_url = f'https://image.tmdb.org/t/p/w500{movie_details['poster_path']}'
    year = movie_details['release_date'].split('-')[0]
    description = movie_details['overview']
    new_movie = Movie(
        title=title,
        year=year,
        description=description,
        img_url=img_url,
    )
    db.session.add(new_movie)
    db.session.commit()
    query_movie = db.session.execute(db.select(Movie).where(Movie.title == new_movie.title)).scalar()
    print(f'Added new movie {title}')
    return query_movie.id


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating.asc()))
    all_movies = result.scalars().all()  # convert ScalarResult to Python List

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get('id')
    query_movie = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    if form.validate_on_submit():
        query_movie.rating = form.data['rating']
        query_movie.review = form.data['review']
        db.session.commit()
        print(f'Edited film {query_movie.title}')
        return redirect(url_for('home'))
    return render_template('edit.html', movie=query_movie, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    db.session.delete(movie_to_delete)
    db.session.commit()
    print(f'Deleted movie {movie_to_delete.title}')
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_title = form.data['title']
        movies = get_movie_list(movie_title)
        return render_template('select.html', movies=movies)
    return render_template('add.html', form=form)


@app.route("/select")
def select():
    movie_db_id = request.args.get('id')
    if movie_db_id:
        movie_details = get_movie_details(int(movie_db_id))
        if movie_details:
            sql_movie_id = add_movie(movie_details)
            return redirect(url_for("edit", id=sql_movie_id))


if __name__ == '__main__':
    app.run(debug=True)
