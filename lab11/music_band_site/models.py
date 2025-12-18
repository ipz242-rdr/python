from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

# 1. Ми створюємо об'єкт db тут, але поки не прив'язуємо до app (це важливо!)
db = SQLAlchemy()

# Таблиця користувачів
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

# Таблиця альбомів
class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    cover_image = db.Column(db.String(100), nullable=True)