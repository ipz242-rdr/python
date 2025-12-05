from lab8_task8 import Shop, Discount
import unittest


class TestShop(unittest.TestCase):

    def setUp(self):

        self.shop = Shop("Сільпо", "Продукти")

    def test_init_success(self):
        self.assertEqual(self.shop.shop_name, "Сільпо")
        self.assertEqual(self.shop.store_type, "Продукти")
        self.assertEqual(self.shop.numbers_of_units, 0)

    def test_init_invalid_name(self):
        with self.assertRaises(ValueError):
            Shop("", "Техніка")

    def test_init_invalid_type(self):
        with self.assertRaises(ValueError):
            Shop("Rozetka", "")

    def test_describe_shop(self):
        expected = "Назва магазину: Сільпо, Тип: Продукти"
        self.assertEqual(self.shop.describe_shop(), expected)

    def test_open_shop(self):
        self.assertEqual(self.shop.open_shop(), "Магазин Сільпо відкритий!!!")

    def test_set_units_success(self):
        msg = self.shop.set_number_of_units("Хліб", 50)
        self.assertEqual(self.shop.numbers_of_units, 50)
        self.assertIn("Кількість на складі: 50", msg)

    def test_set_units_negative(self):
        with self.assertRaises(ValueError):
            self.shop.set_number_of_units("Хліб", -10)

    def test_increment_units(self):
        self.shop.set_number_of_units("Хліб", 10)  # Було 10
        self.shop.increment_number_of_units(5)  # Додали 5
        self.assertEqual(self.shop.numbers_of_units, 15)  # Стало 15

    def test_discount_products_list(self):
        products = ["Яблука", "Банани"]
        disc_shop = Discount("Фора", "Продукти", products)

        result = disc_shop.get_discount_products()
        self.assertEqual(result, "Товари зі знижкою: Яблука, Банани")

    def test_discount_empty(self):
        disc_shop = Discount("Фора", "Продукти", [])
        self.assertEqual(disc_shop.get_discount_products(), "Немає товарів зі знижкою")


if __name__ == '__main__':
    unittest.main()
