import re


class Apple:
    states =["Відсутнє", "Цвітіння", "Зелене", "Червоне"]

    def __init__(self, _index):
        self.error_in_class_Apple = []

        if not isinstance(_index, int):
            self.error_in_class_Apple.append("Індекс не може бути порожній")
        elif 0 > _index:
            self.error_in_class_Apple.append("Індекс має бути більше 0")
        else:
            self._index = _index
            self._state = self.states[0]

        if self.error_in_class_Apple:
            print("Помилки")
            for error in self.error_in_class_Apple:
                print(f"{error}")
            raise SystemExit(1)

    def grow(self):
        current_index = self.states.index(self._state)
        if current_index < len(self.states) - 1:
            self._state = self.states[current_index + 1]
        else:
            print(f"Яблуко {self._index} - стигле")

    def is_ripe(self):
        if self._state == self.states[-1]:
            return f"Яблуко {self._index} достигло"


class AppleTree:
    def __init__(self, count_apple):
        self.error_in_class_AppleTree = []

        if not isinstance(count_apple, int):
            self.error_in_class_AppleTree.append("Кількість якблук має бути числом")
        elif 0 > count_apple:
            self.error_in_class_AppleTree.append("Кільксть яблук не може бути від'ємною")
        else:
            self.apples = [Apple(i) for i in range(count_apple)]

        if self.error_in_class_AppleTree:
            print("Помилки")
            for error in self.error_in_class_AppleTree:
                print(f"{error}")
            raise SystemExit(1)

    def grow_all(self):
        for apple in self.apples:
            apple.grow()

    def all_are_ripe(self):
        if all(apple.is_ripe() for apple in self.apples):
            return True

    def give_away_all(self):
        self.apples.clear()
        print("Зібрано врожай, Список яблук порожній")


class Gardener:
    def __init__(self, name, _tree):
        self.error_in_class_Gardener = []

        name_true_symbol = re.compile(r"^[A-Za-zА-Яа-яІіЇїЄєҐґ\'-]+$")
        if not isinstance(name, str) or not name.strip():
            self.error_in_class_Gardener.append("Ім'я не може бути порожнім рядком")
        elif not name_true_symbol.fullmatch(name.strip()):
            self.error_in_class_Gardener.append("Ім'я не може містити незрозумілі символи")
        else:
            self.name = name.strip()

        if not isinstance(_tree, AppleTree):
            self.error_in_class_Gardener.append("_tree має бути об'єктом AppleTree")
        else:
            self._tree = _tree

        if self.error_in_class_Gardener:
            print("Помилки")
            for error in self.error_in_class_Gardener:
                print(f"{error}")
            raise SystemExit(1)

    def work(self):
        print(f"{self.name} почав працювати ")
        self._tree.grow_all()

    def harvest(self):
        if self._tree.all_are_ripe():
            print(f"{self.name} почав збирати урожай, адже всі яблука дозріли")
            self._tree.give_away_all()
        else:
            print("яблука ще не дозріли, треба почекати")

    @staticmethod
    def apple_base():
        print("Чи дозрів урожай")
        for i, state in enumerate(Apple.states):
            print(f"{i}: {state}")


apple1 = Apple(1)
apple2 = Apple(2)
apple3 = Apple(3)

Gardener.apple_base()

tree = AppleTree(3)
gardener = Gardener("Микола", tree)
print("Cадівник працює")
gardener.work()
print("Спробуємо зібрати урожай")
gardener.harvest()
print("ще є недозрілі яблука треба почекати")
while not gardener._tree.all_are_ripe():
    gardener.work()
    if gardener.harvest():
        break

print(f"Залишилось яблук на дереві: {len(gardener._tree.apples)}")
