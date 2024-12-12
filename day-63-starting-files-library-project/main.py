from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)


class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    review: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    result = db.session.execute(db.select(Books).order_by(Books.title))
    all_books = result.scalars()
    is_book_in_table = db.session.query(Books).first()  # check if there is a first row in table (emptiness proof)
    return render_template('index.html', books=all_books, occupied=is_book_in_table)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        form_title = request.form['title']
        form_author = request.form['author']
        form_rating = request.form['rating']
        book = Books(title=form_title, author=form_author, review=form_rating)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template('add.html')


@app.route("/edit", methods=["GET", "POST"])
def edit():
    book_id = request.args.get('id')
    query_book = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    if request.method == 'POST':
        query_book.review = request.form['new_rating']
        db.session.commit()
        return redirect(url_for("home"))
    return render_template('edit.html', book=query_book)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    book_to_delete = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
