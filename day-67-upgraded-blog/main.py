from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from flask_ckeditor.utils import cleanify
from datetime import date

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['CKEDITOR_SERVE_LOCAL'] = True
Bootstrap5(app)
ckeditor = CKEditor(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


# Configure form to create the blog post
class NewBlogPostForm(FlaskForm):
    blog_post_title = StringField('Blog Post Title', validators=[DataRequired()])
    blog_post_subtitle = StringField('Subtitle', validators=[DataRequired()])
    authors_name = StringField('Your Name', validators=[DataRequired()])
    url_img = StringField('Blog Image URL', validators=[URL()])
    body = CKEditorField('Blog Content', validators=[DataRequired()])
    submit = SubmitField('SUBMIT POST')


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)


# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/new-post", methods=['GET', 'POST'])
def make_post():
    form = NewBlogPostForm()
    if form.validate_on_submit():

        new_blog_post = BlogPost(
            title=form.blog_post_title.data,
            subtitle=form.blog_post_subtitle.data,
            author=form.authors_name.data,
            img_url=form.url_img.data,
            body=cleanify(form.body.data),
            date=date.today().strftime('%B %d, %Y')
        )
        db.session.add(new_blog_post)
        db.session.commit()

        return redirect(url_for('get_all_posts'))
    else:
        return render_template("make-post.html", form=form, new_post=True)


# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<post_id>", methods=['GET', 'POST'])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = NewBlogPostForm(
        blog_post_title=post.title,
        blog_post_subtitle=post.subtitle,
        authors_name=post.author,
        url_img=post.img_url,
        body=post.body,
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.blog_post_title.data
        post.subtitle = edit_form.blog_post_subtitle.data
        post.author = edit_form.authors_name.data
        post.img_url = edit_form.url_img.data
        post.body = cleanify(edit_form.body.data)
        db.session.commit()
        return render_template("post.html", post=post)
    else:
        return render_template("make-post.html", new_post=False, form=edit_form)


# TODO: delete_post() to remove a blog post from the database
@app.route("/delete/<post_id>")
def delete_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    if post:
        db.session.delete(post)
        db.session.commit()
    return redirect(url_for('get_all_posts'))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
