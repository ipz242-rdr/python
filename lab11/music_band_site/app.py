from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
# Вказуємо шлях, де буде лежати файл бази даних (music.db)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'

# Ініціалізуємо базу даних
db = SQLAlchemy(app)

# Ініціалізуємо менеджер логіну (для авторизації)
login_manager = LoginManager(app)
login_manager.login_view = 'login' # Куди перенаправляти, якщо юзер не зайшов

@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)