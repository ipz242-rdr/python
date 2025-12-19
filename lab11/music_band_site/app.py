from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, date
from models import db, User, Album

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'


db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# --- МАРШРУТИ ---

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Неправильний логін або пароль')

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/albums')
def albums():
    all_albums = Album.query.all()
    return render_template('albums.html', albums=all_albums)


@app.route('/album/new', methods=['GET', 'POST'])
@login_required
def create_album():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        cover_url = request.form['cover']

        date_str = request.form['release_date']

        try:
            # Цей рядок каже: "Візьми текст date_str і прочитай його як Рік-Місяць-День"
            release_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            return "Помилка формату дати", 400

            # --- ПЕРЕВІРКА НА МАЙБУТНЄ ---
        if release_date > date.today():
            flash(f"Помилка: Дата не може бути в майбутньому! (Сьогодні {date.today()})")
            return render_template('create_album.html')

        new_album = Album(title=title, release_date=release_date, description=description, cover_image=cover_url)

        db.session.add(new_album)
        db.session.commit()

        return redirect(url_for('albums'))

    return render_template('create_album.html')

@app.route('/album/<int:id>/delete')
@login_required
def delete_album(id):
    album_to_delete = Album.query.get_or_404(id)

    try:
        db.session.delete(album_to_delete)
        db.session.commit()
        return redirect(url_for('albums'))
    except:
        return "Сталася помилка при видаленні альбому"

@app.route('/album/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_album(id):
    album = Album.query.get_or_404(id)

    if request.method == 'POST':
        album.title = request.form['title']
        album.year = request.form['year']
        album.description = request.form['description']
        album.cover_image = request.form['cover']

        try:
            db.session.commit()
            return redirect(url_for('albums'))
        except:
            return "Помилка редагування"

    return render_template('edit_album.html', album=album)

@app.route('/album/<int:id>')
def album_detail(id):
    album = Album.query.get_or_404(id)
    return render_template('album_detail.html', album=album)

@app.route('/history')
def history():
    return render_template('history.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)