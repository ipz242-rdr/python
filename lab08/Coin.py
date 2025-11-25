import random


class Coin:
    def __init__(self):
        self.__sideup = 'heads'
        if self.__sideup not in ["heads", "tails"]:
            print("Сторона має бути 'heads' або 'tails'")
            return

    def toss(self):
        self.__sideup = random.choice(["heads", "tails"])
        return self.__sideup

    def get_sideup(self):
        return self.__sideup


def task2():
    coin = Coin()
    n = 10
    for i in range(n):
        result = coin.toss()
        print(f"Підкидання № {i + 1}: Результат: {result}")


task2()
