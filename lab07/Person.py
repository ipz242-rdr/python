import csv
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

    def get_age(self) -> int:
        today = date.today()
        birth_date = self.birth_date
        get_date = today.year - self.birth_date.year
        if(today.month, today.day) < (birth_date.month, birth_date.day):
            get_date -= 1

        return get_date


try:
        contact1 = Person(
        surname="Руденко",
        first_name="Дмитро",
        date_string="2007-06-24",
        nickname="jaster"
    )
        print(contact1.get_fullname())
        print("Повних років:", contact1.get_age())
except TypeError as e:
    print(f"Помилка вхідних даних: {e}")


def modifier(filename):
    all_data = []
    with open(filename, "r", newline='', encoding='UTF-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        try:
            surname_ind = header.index("surname")
            name_ind = header.index("first_name")
            date_ind = header.index("birth_date")
            nick_name_ind = header.index("nickname")
        except ValueError as e:
            raise ValueError(f"Файл не містить обов'язковї колонки: {e}")
        for row in reader:
            try:
                person_obj = Person(
                    surname=row[surname_ind],
                    first_name=row[name_ind],
                    date_string=row[date_ind],
                    nickname=row[nick_name_ind],
                )
                fullname = f"{person_obj.first_name} {person_obj.surname}, Псевдонім: {person_obj.nickname}"
                row.insert(name_ind + 1, fullname)

                age = person_obj.get_age()
                row.append(age)
                all_data.append(row)
            except (TypeError, ValueError) as e:
                print(f"Помилка обробки рядка {row}: {e}")
                continue
    header.insert(name_ind + 1, 'fullname')
    header.append('age')

    with open(filename, "w", newline='', encoding='UTF-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(all_data)
        print(f"файл '{filename}' успішно доданий вміст")


modifier('test_contacts.csv')

# surname,first_name,fullname,nickname,birth_date
# Григоренко,Наталя,Наталя Григоренко,Ната,1985-06-15
# Іваненко,Петро,Петро Іваненко,,2000-11-25
# Шевченко,Ольга,Ольга Шевченко,Оля,2010-12-31
