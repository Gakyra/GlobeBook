from flask_login import UserMixin
from app import db

# Модель користувача
class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Модель туру
class Tour(db.Model):
    __tablename__ = 'tour'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    available_spots = db.Column(db.Integer, nullable=False)

# Модель бронювання
class Booking(db.Model):
    __tablename__ = 'booking'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tour_id = db.Column(db.Integer, db.ForeignKey('tour.id'), nullable=False)
    number_of_people = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
