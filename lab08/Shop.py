class Shop:
    def __init__(self, shop_name, store_type):
        if not isinstance(shop_name, str) or not shop_name.strip():
            raise ValueError("Назва магазину не може бути порожньою ")
        if not isinstance(store_type, str) or not store_type.strip():
            raise ValueError("Магазин має продавати речі певного типу")

        self.shop_name = shop_name
        self.store_type = store_type
        self.numbers_of_units = 0

    def describe_shop(self):
        return f"Назва магазину: {self.shop_name}, Тип: {self.store_type}"

    def open_shop(self):
        return f"Магазин {self.shop_name} відкритий!!!"

    def set_number_of_units(self, name_goods, new_number):
        if not isinstance(name_goods, str) or not name_goods.strip():
            raise ValueError("Назва товару не може бути пустим рядком")
        if not isinstance(new_number, int) or new_number < 0:
            raise ValueError("Кількість товару має бути цілим числом більшим за 0")
        self.numbers_of_units = new_number
        return f"Магазин: {self.shop_name}, Товар: {name_goods}, Кількість на складі: {self.numbers_of_units}"

    def increment_number_of_units(self, amount):
        if not isinstance(amount, int) or amount < 0:
            raise ValueError("Кількість товару має бути числом більшим за 0")
        self.numbers_of_units += amount
        return f"Кількість доданого товару на склад: {amount}. Поточна кількість: {self.numbers_of_units}"


class Discount(Shop):
    def __init__(self, shop_name, store_type, discount_percent):
        super().__init__(shop_name, store_type)
        self.discount_percent = discount_percent

    def get_discount_products(self):
        if not self.discount_percent:
            return "Немає товарів зі знижкою"
        return f"Товари зі знижкою: {', '.join(self.discount_percent)}"



