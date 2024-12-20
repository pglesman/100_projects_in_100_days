from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func


'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        # Loop through each column in the data record, create a new dictionary entry where the key
        # is the name of the column and the value is the value of the column
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    # pick random row from database, use sqlalchemy 'random' function to optimize picking
    random_cafe = db.session.execute(db.select(Cafe).order_by(func.random()).limit(1)).scalar()
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def get_all_cafes():
    # pick random row from database, use sqlalchemy 'random' function to optimize picking
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return jsonify(cafe=[cafe.to_dict() for cafe in all_cafes])


@app.route("/search")
def search_cafe():
    search_location = request.args.get('loc').title()
    query_cafes = db.session.execute(db.select(Cafe).where(Cafe.location == search_location)).scalars().all()
    if query_cafes:
        return jsonify(cafe=[cafe.to_dict() for cafe in query_cafes])
    else:
        return jsonify(error={
            'Not Found': f'Sorry, we don\'t have a cafe at that location: {search_location}'
        })

# HTTP POST - Create Record


@app.route("/add", methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get('name'),
        map_url=request.form.get('map', default=''),
        img_url=request.form.get('img', default=''),
        location=request.form.get('loc', default=''),
        seats=request.form.get('seats', default=''),
        has_toilet=bool(request.form.get('toilet', default=False)),
        has_wifi=bool(request.form.get('wifi', default=False)),
        has_sockets=bool(request.form.get('sockets', default=False)),
        can_take_calls=bool(request.form.get('calls', default=False)),
        coffee_price=request.form.get('price', default=''),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(success=f'Successfully added the new cafe: {new_cafe.name}')


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=['PATCH'])
def update_price(cafe_id):
    new_price = request.args.get('new_price')
    cafe = db.get_or_404(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(success="Successfully updated the price")
    else:
        return jsonify(error={'Not Found': f"Sorry, a cafe with that id {cafe_id} was not found in the database"})


# HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=['DELETE'])
def delete_cafe(cafe_id):
    api_key = request.args.get('api-key')
    if api_key != 'TopSecretAPIKey':
        return jsonify(error={"Forbidden": "Sorry, that is not allowed. Make sure you have the correct api_key"})
    cafe = db.get_or_404(Cafe, cafe_id)
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(success="Successfully deleted a cafe")
    else:
        return jsonify(error={'Not Found': f"Sorry, a cafe with that id {cafe_id} was not found in the database"})


if __name__ == '__main__':
    app.run(debug=True)
