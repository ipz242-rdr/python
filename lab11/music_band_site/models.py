from app import db
from flask_login import UserMixin

# Таблиця користувачів (адмінів)
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

# Таблиця альбомів
class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False) # Назва альбому
    year = db.Column(db.Integer, nullable=False)      # Рік випуску
    description = db.Column(db.Text, nullable=True)   # Опис
    cover_image = db.Column(db.String(100), nullable=True) # Назва файлу картинки