from User import User

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