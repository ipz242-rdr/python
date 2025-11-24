from datetime import date


class Car:
    def __init__(self, mark: str, model: str, year_create: int):
        if not isinstance(mark, str) or not mark.strip():
            raise ValueError("Мфрка автомобіля не може бути порожнім рядком")
        if any(char.isdigit() for char in mark):
            raise ValueError("Марка автомобіля не має складатись із цифр")

        if not isinstance(model, str) or not model.strip():
            raise ValueError("Модель автомобіля не може бути порожнім рядком")
        if any(char.isdigit() for char in model):
            raise ValueError("Модель автомобіля не має складатись із цифр")

        if not isinstance(year_create, int):
            raise ValueError("Рік повинен бути цілим числом")
        if year_create < 1880:
            raise ValueError("Рік повинен бути більшим за 1880")
        if year_create > date.today().year:
            raise ValueError("Рік не може бути з майбутнього")

        self.mark = mark
        self.model = model
        self.year_create = year_create
        self.speed = 0

    def accelerate(self):
        self.speed = self.speed + 5
        return self.speed

    def brake(self):
        self.speed = max(0, self.speed - 5)
        return self.speed

    def get_speed(self):
        return self.speed


def task03():
    car = Car(
        mark="Mercedes-Benz",
        model="E-Class W212",
        year_create=2014,
    )

    print(f"Автомобіль: {car.mark} {car.model}, Рік: {car.year_create}")
    for i in range(5):
        car.accelerate()
        print(f"Машину прискорено поточна швидкість {car.get_speed()}")

    for i in range(5):
        car.brake()
        print(f"Машину пригальмовано поточна швидкість {car.get_speed()}")


task03()
