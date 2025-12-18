from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

# --- ВАЖЛИВО: Імпортуємо db та класи з models.py ---
from models import db, User, Album

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'

# --- ЗВ'ЯЗУЄМО БАЗУ З ДОДАТКОМ ---
# Раніше тут було db = SQLAlchemy(app), тепер ми ініціалізуємо існуючу db:
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

        # Тепер User.query буде працювати коректно
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


if __name__ == '__main__':
    # Створюємо таблиці, якщо їх ще немає (автоматично при запуску)
    with app.app_context():
        db.create_all()
    app.run(debug=True)