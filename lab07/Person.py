from datetime import date


class Person:
    def __init__(self, surname: str, first_name: str, date_string: str, nickname: str = None):
        if not isinstance(surname, str):
            raise TypeError("Атрибут 'surname' має бути типу (str)")
        if not isinstance(first_name, str):
            raise TypeError("Атрибут 'first_name' має бути типу (str)")
        if not isinstance(date_string, str):
            raise TypeError("Атрибут 'date_string' має бути типу (str)")
        self.surname = surname
        self.first_name = first_name

        try:
            parts = date_string.split('-')
            year_int = int(parts[0])
            month_int = int(parts[1])
            day_int = int(parts[2])
            birth_date_obj = date(year_int, month_int, day_int)
        except ValueError:
            raise ValueError("Неправильний формат дати. Використовуйте 'YYYY-MM-DD'.")
        except IndexError:
            raise ValueError("Неправильний формат дати. Використовуйте 'YYYY-MM-DD'.")
        self.birth_date = birth_date_obj
        self.nickname = nickname

    def get_fullname(self):
        info = f"Контакт: {self.first_name} {self.surname}, Псевдонім: {self.nickname}"
        return info

    def get_age(self):
        today = date.today()
        birth_date = self.birth_date
        get_date = today.year - self.birth_date.year
        if(today.month, today.day) < (birth_date.month, birth_date.day):
            get_date -= 1
        print_old = f"Поточний вік користувача {get_date}"
        return print_old


try:
        contact1 = Person(
        surname="Руденко",
        first_name="Дмитро",
        date_string="2007-06-24",
        nickname="jaster"
    )
        print(contact1.get_fullname())
        print(contact1.get_age())
except TypeError as e:
    print(f"Помилка вхідних даних: {e}")


