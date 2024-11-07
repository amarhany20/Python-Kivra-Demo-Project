from .database import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    userId = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)
    update_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Location(db.Model):
    __tablename__ = 'locations'
    location_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.userId'), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    post_code = db.Column(db.String(10), nullable=False)

class Type(db.Model):
    __tablename__ = 'types'
    type_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.userId'), nullable=False)

class Mail(db.Model):
    __tablename__ = 'mails'
    mail_id = db.Column(db.Integer, primary_key=True)
    sender_user_id = db.Column(db.Integer, db.ForeignKey('users.userId'), nullable=False)
    receiver_user_id = db.Column(db.Integer, db.ForeignKey('users.userId'), nullable=False)
    date_time = db.Column(db.DateTime, default=datetime.utcnow)
    received = db.Column(db.Boolean, default=False)
    opened = db.Column(db.Boolean, default=False)
    type = db.Column(db.String(50), nullable=False)
    mail_save_location = db.Column(db.String(255), nullable=True)
