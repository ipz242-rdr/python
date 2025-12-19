from app import app, db
from models import User
from werkzeug.security import generate_password_hash

# Цей блок коду спрацює, коли ти запустиш цей файл
with app.app_context():
    # 1. Створюємо таблиці (якщо їх нема)
    db.create_all()

    # 2. Перевіряємо, чи є вже адмін, щоб не створити дублікат
    if not User.query.filter_by(username='admin').first():
        hashed_pw = generate_password_hash('123')
        admin = User(username='admin', password=hashed_pw)
        db.session.add(admin)
        db.session.commit()
        print("Супер! Адміністратора 'admin' створено.")
    else:
        print("Адміністратор вже існує. Нічого робити не треба.")