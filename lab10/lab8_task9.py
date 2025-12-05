class User:
    def __init__(self, first_name, last_name, email, nickname, newsletter_subscription=True):
        if not isinstance(first_name, str) or not first_name.strip():
            raise ValueError("Ім'я не може бути порожнім і повинно бути рядком")
        if not isinstance(last_name, str) or not last_name.strip():
            raise ValueError("Прізвище не може бути порожнім і повинно бути рядком")
        if not isinstance(email, str) or not email.strip():
            raise ValueError("Email не може бути порожнім і повинно бути рядком")
        if not isinstance(nickname, str) or not nickname.strip():
            raise ValueError("Нікнейм не може бути порожнім і повинно бути рядком")
        if not isinstance(newsletter_subscription, bool):
            raise ValueError("Згода на розсилку має бути булевим значенням")

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.nickname = nickname
        self.newsletter_subscription = newsletter_subscription
        self.login_attempts = 0

    def describe_user(self):
        return f"Користувач, {self.first_name}"

    def greeting_user(self):
        return f"привіт, {self.first_name}. Ласкаво просимо"

    def increment_login_attempts(self):
        self.login_attempts += 1
        return f"Спроби входу: {self.login_attempts}"

    def reset_login_attempts(self):
        self.login_attempts = 0
        return f"Спроби входу після скидання: {self.login_attempts}"


class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = []
        if not isinstance(privileges, list):
            raise ValueError("Privileges має бути списком рядків")
        self.privileges = privileges

    def show_privileges(self):
        if not self.privileges:
            return "У адміністратора немає привілеїв"
        return "Привілеї адміністратора: \n " + "\n-".join(self.privileges)


class Admin(User):
    def __init__(self, first_name, last_name, email, nickname, newsletter_subscription=True):
        super().__init__(first_name, last_name, email, nickname, newsletter_subscription)
        default_privileges = [
            "Дозволено додавати повідомлення",
            "Дозволено видаляти користувачів",
            "Дозволено блокувати користувачів",
            "Дозволено змінювати налаштування"
        ]
        self.priv = Privileges(default_privileges)
