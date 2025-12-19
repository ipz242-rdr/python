from . import db

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    description = db.Column(db.Text, nullable=True)
    cover_image = db.Column(db.Text, nullable=True)