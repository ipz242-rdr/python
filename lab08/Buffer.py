import time
from typing import List


class Buffer:
    def __init__(self):
        self.buffer: List[int] = []

    def add(self, *a: int):
        print(f"\n Отримано нову частину: {list(a)}")

        for item in a:
            if isinstance(item, int):
                self.buffer.append(item)
            else:
                print(f"Помилка: Пропущено неціле значення: {item}")

        while len(self.buffer) >= 5:
            chunk = self.buffer[0:5]
            chunk_sum = sum(chunk)

            print(f" Об'єднано: {chunk}, Сума: {chunk_sum}")

            self.buffer = self.buffer[5:]

        print(f" Залишок у буфері ({len(self.buffer)} елементів): {self.buffer}")

    def get_current_part(self) -> List[int]:
        return self.buffer


if __name__ == '__main__':
    data_buffer = Buffer()

    print(" Додаємо 3 елементи ")
    data_buffer.add(1, 2, 3)
    time.sleep(0.5)

    print("\n Додаємо 6 елементів ")
    data_buffer.add(4, 5, 6, 7, 8, 9)
    time.sleep(0.5)

    print("\n Додаємо 2 елементи ")
    data_buffer.add(10, 11)
    time.sleep(0.5)

    print("\n Додаємо 10 елементів (Подвійна обробка) ")
    data_buffer.add(12, 13, 14, 15, 16, 17, 18, 19, 20, 21)

    print("\nСТАН БУФЕРА")
    final_part = data_buffer.get_current_part()
    print(f"Кінцевий залишок: {final_part}")
