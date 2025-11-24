class Dog:
    mammal = True
    nature = "Характер невідомий"
    breed_default = "невідома порода"

    def __init__(self, name, age, breed):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Ім'я собаки не повинно бути порожнім")
        if not isinstance(age, (int, float)):
            raise ValueError("Вік собаки не може бути числом")
        if age < 0 or age > 30:
            raise ValueError("Вік собаки не може бути від'ємним та не може бути більше 30")
        if not isinstance(breed, str) or not breed.strip():
            raise ValueError("Порода собаки не може бути порожнім текстом")
        if any(char.isdigit() for char in breed):
            raise ValueError("Порода не може містити цифри")

        self.name = name
        self.age = age
        self.breed = breed

    def get_info(self):
        return f"Ім'я: {self.name}, Порода: {self.breed}, Вік: {self.age}"

    def behavior(self):
        return f"{self.name}: Гарчання собаки"


class GermanShepherd(Dog):
    nature = "Розумний, хитрий"
    breed_default = "Німецька вівчарка"

    def __init__(self, name, age):
        super().__init__(name, age, breed="Німецька вівчарка")

    def clever(self):
        return f"{self.name}: Дуже розумний і хитрий собака"


class Malinois(Dog):
    nature = "Витривалий, сильний"
    breed_default = "Малінуа"

    def __init__(self, name, age):
        super().__init__(name, age, breed="Малінуа")

    def strong(self):
        return f"{self.name}: Швидка сильний та витривалий собака"


class Pug(Dog):
    nature = "Веселий, спокійний"
    breed_default = "Мопс"

    def __init__(self, name, age):
        super().__init__(name, age, breed="Мопс")

    def snore(self):
        return f"{self.name}: Спить і голосно хропе"


class Pets:
    def __init__(self):
        self.pet_list = []

    def add_pet(self, pet_obj):
        if isinstance(pet_obj, Dog):
            self.pet_list.append(pet_obj)
        else:
            print(f"Помилка: {pet_obj.name} не є собакою")

    def display_all_pets(self):
        print("ВСЯ ІНФА ПРО ТВАРИН")
        for pet in self.pet_list:

            print(f"\n{pet.breed} Ссавець:{pet.mammal}")
            pet.get_info()

            print(f"Голос: {pet.behavior()}")

            if isinstance(pet, GermanShepherd):
                print(f"Особливість: {pet.clever()}")
            if isinstance(pet, Malinois):
                print(f"Особливість: {pet.strong()}")
            if isinstance(pet, Pug):
                print(f"Особливість: {pet.snore()}")


rex = Malinois(name="Рекс", age=5)
bella = Pug(name="Белла", age=2)
max_dog = GermanShepherd(name="Макс", age=8)

my_animals = Pets()

my_animals.add_pet(rex)
my_animals.add_pet(bella)
my_animals.add_pet(max_dog)

my_animals.display_all_pets()
