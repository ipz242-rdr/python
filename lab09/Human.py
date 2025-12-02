import re


class Human:
    default_name = "Користувач"
    default_age = 0
    good_symbols_in_text = re.compile(r"^[A-Za-zА-Яа-яІіЇїЄєҐґ\'-]+$")

    def __init__(self, name: str, age: int, money=0, house=None):
        self.error_in_class_Numan = []

        if not isinstance(name, str) or not name.strip():
            self.error_in_class_Numan.append("Ім'я не може бути пустим рядком")
        elif not self.good_symbols_in_text.fullmatch(name.strip()):
            self.error_in_class_Numan.append("Недопустимі символи в ім'ї")
        else:
            self.name = name

        if not isinstance(age, int):
            self.error_in_class_Numan.append("Вік має бути цілим числом")
        elif 0 > age or age > 130:
            self.error_in_class_Numan.append("Ви ввели неможливий вік")
        else:
            self.age = age

        if not isinstance(money, (int, float)):
            self.error_in_class_Numan.append("Гроші мають бути числом")
        elif 0 > money:
            self.error_in_class_Numan.append("Гроші не можуть бути від'ємними")
        else:
            self._money = money

        if not isinstance(house, House) and house is not None:
            self.error_in_class_Numan.append("house має бути об'єктом House")
        else:
            self._house = house

        if self.error_in_class_Numan:
            print("Помилки")
            for error in self.error_in_class_Numan:
                print(f"{error}")
            raise SystemExit(1)

    def info(self):
        return (f"Ім'я: {self.name}, Вік: {self.age}, Гроші:{self._money:.2f}) " +
                f" Будинок: Площа{self._house._area if self._house else ' немає будинку'} m^2")

    @staticmethod
    def default_info():
        print(f"Значення за замовчуванням: Ім'я: {Human.default_name}, Вік:{Human.default_age}")

    def _make_deal(self, house, price):
        self._money -= price
        self._house = house

    def earn_money(self, cash):
        if not isinstance(cash, (int, float)) or cash < 0:
            print("Некоректне введення коштів")
            raise SystemExit(1)
        self._money += cash
        return f"Додано {cash} грошей"

    def buy_house(self, house, discount=10):
        if not isinstance(house, House):
            print("house має бути об'єктом House")
            raise SystemExit(1)
        if not (0 <= discount <= 100):
            print("Знижка має бути від 0% до 100%")
            raise SystemExit(1)
        cost_house_with_discount = house.final_price(discount)

        if self._money < cost_house_with_discount:
            need_money = cost_house_with_discount - self._money
            return f"у вас недостатньо коштів. Ще потрібно {need_money}"
        else:
            self._make_deal(house, cost_house_with_discount)
            return "будинок купленою Вітаємо з покупкою"


class House:
    def __init__(self, _area=70, _price=70000):
        self.error_in_class_House = []

        if not isinstance(_area, (int, float)):
            self.error_in_class_House.append("Площа має бути числом")
        elif _area <= 0:
            self.error_in_class_House.append("Площа не може бути 0 або менше нуля")
        else:
            self._area = float(_area)

        if not isinstance(_price, (int, float)):
            self.error_in_class_House.append("Ціна має бути числом")
        elif _price <= 0:
            self.error_in_class_House.append("Ціна не може бути 0 або менше нуля")
        else:
            self._price = float(_price)

        if self.error_in_class_House:
            print("Помилки")
            for error in self.error_in_class_House:
                print(f"{error}")
                raise SystemExit(1)

    def final_price(self, discount):
        if not isinstance(discount, (int, float)):
            print("Знижка має бути цілим або дробовим числом")
            raise SystemExit(1)
        elif discount < 0 or discount > 100:
            print("Знижка має бути від 0% до 100%")
            raise SystemExit(1)
        return self._price * (1 - discount / 100)


class SmallHouse(House):
    def __init__(self):
        super().__init__(_area=40, _price=40000)


human = Human("Петро", 20, 12000)
Human.default_info()
print(human.info())
small_house = SmallHouse()
print(human.buy_house(small_house, 20))
print(human.earn_money(22000))
print(human.buy_house(small_house, 20))
print(human.info())
