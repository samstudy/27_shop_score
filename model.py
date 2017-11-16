from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://score:Rysherat2@shopscore.devman.org:5432/shop'
db = SQLAlchemy(app)


class Orders(db.Model):
    __tablename__ = 'orders'
    created = db.Column(db.DateTime, primary_key = True)
    status = db.Column(db.Text)
    confirmed = db.Column(db.DateTime)