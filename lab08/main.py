from Shop import Shop, Discount
shop = Shop("Comfy", "Електроніка")
print(f"\n Назва: {shop.shop_name}")
print(f"\n Тип: {shop.store_type}")
print(shop.describe_shop())
print(shop.open_shop())

store1 = Shop("ATБ", "Продуктовий")
store2 = Shop("Brain", "Електроніка")
store3 = Shop("Flowers", "Квітковий")
print("\n", store1.describe_shop())
print(store2.describe_shop())
print(store3.describe_shop())

store = Shop("Сільпо", "Продуктовий")
print(f"Початкова кількість певного товару {store.numbers_of_units} в магазині {store.shop_name}")
store.numbers_of_units = 25
print(f"Кількість певного товару після зміни {store.numbers_of_units} в магазині {store.shop_name}")
store.set_number_of_units("Ковбаса", 20)
print(store.set_number_of_units("Ковбаса", 20))
print(store.increment_number_of_units(10))

store_discount = Discount("Comfy", "Електроніка", ["Телевізор", "Навушники"])
print(store_discount.get_discount_products())

all_store = Shop("EpicStore", "Iгрові товари")
print(all_store.describe_shop())
