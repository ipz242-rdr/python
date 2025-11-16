import  os
import time
from typing import List
import datetime
import re
from collections import Counter
import math

def task1():
    numbers = []
    try:
        with open("numbers.txt", "r") as myfile:
            for line in myfile:
                cleaned_line = line.strip()
                if cleaned_line:
                    try:
                        number = int(cleaned_line)
                        numbers.append(number)
                    except ValueError:
                        print(f"Помилка: не числове значення {cleaned_line}")
    except ValueError:
        print("Помилка: файл numbers.txt не знайдено, або він не існує")
        return
    total_sum = sum(numbers)
    print(f"Сума чисел у файлі: {total_sum}")
    try:
        with open("sum_numbers.txt", "w") as file_out:
            file_out.write(str(total_sum))
    except Exception as e:
        print(f"Помилк апри записі у файл {e}")


def task2():
    text_user = (input("Введіть цілі числа через пробіл: ").strip()).split()
    numbers = []
    for n in text_user:
        try:
            numbers.append(int(n))
        except ValueError:
            print(f"{n} не є цілим числом, тому ми його пропустимо")
    if not numbers:
        print("Ви нічого не ввели")
        return

    with open("numbers_task2.txt", "w", encoding="UTF-8") as file_num:
        for num in numbers:
            if num % 2 == 0:
                file_num.write(f"{num} - парне число\n")
            else:
                file_num.write(f"{num} - не парне число\n")


def task3():
    with open("learning_python.txt", "r", encoding="UTF-8") as myfile:
        lines = [line.strip() for line in myfile if line.strip()]
    print("Вміст файлу: ")
    for line in lines:
        print(line)
    sorted_lines = sorted(lines, key=len, reverse=True)
    print("вміст після сортування")
    for line in sorted_lines:
        print(line)


def task4():
    file_input = "learning_python.txt"
    new_katalog = "new_folder"
    file_true = os.path.join(new_katalog, "file_true.txt")
    file_false = os.path.join(new_katalog, "file_false.txt")
    with open(file_input, "r", encoding="UTF-8") as file:
        lines = [line.strip() for line in file if line.strip()]

    lines_true = []
    lines_false = []

    for line in lines:
        new_line = line.replace("Python", "C")
        print(f"{new_line}")
        while True:
            answer_task = input("Чи правильна ця фраза для мови С yes/no: ").strip().lower()
            if answer_task in ["y", "yes"]:
                lines_true.append(new_line)
                break
            elif answer_task in ["n", "no"]:
                lines_false.append(new_line)
                break
            else:
                print("Введіть (yes або no)")
    with open(file_true, "w", encoding="UTF-8") as filetrue:
        filetrue.write("\n".join(lines_true))
    with open(file_false, "w", encoding="UTF-8") as filefalse:
        filefalse.write("\n".join(lines_false))
    print(f"результат записано в {new_katalog}")

def task5():
    file_name = "guest_book.txt"
    if not os.path.exists(file_name):
        with open(file_name, "w", encoding="UTF-8") as file:
            create_time = datetime.datetime.now().strftime("%Y-%m-%d %H-:%M:%S")
            file.write(f"Створено файл: {create_time}\n")
    while True:
        name_people = input("Введіть ім'я (або 'вихід' щоб завершити): ")
        if name_people.lower() == "вихід":
            break
        greeting = f"Привіт {name_people}!"
        print(greeting)
        with open(file_name, "a", encoding="UTF-8") as file:
            time_now = datetime.datetime.now().strftime("%Y-%m-%d %H-:%M:%S")
            file.write(f"[{time_now}] {greeting}\n")
    with open(file_name, "a", encoding="UTF-8") as file:
        last_time = datetime.datetime.now().strftime
        file.write(f"Останні зміни: {last_time}\n")


def task6():
    file_name = "3000words_file.txt"
    result_file = "analys_res.txt"
    start_time = time.time()
    start_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H-:%M:%S")

    with open(file_name, "r", encoding="UTF-8") as file:
        text_in_file = file.read().strip()
    if not text_in_file:
        print("Файл порожній")
        return
    if not re.search(r"[a-zA-Z]", text_in_file):
        print("Текст не містить англійських літер(слів)")
        return
    text_in_file_lower = text_in_file.lower()
    all_words = re.findall(r"[a-zA-Z]+", text_in_file_lower)
    words_count = len(all_words)
    print(f"У файлі міститься {words_count} cлів")

    if words_count > 3000:
        print(f"У файлі більше ніж 3000 слів({words_count}), скоротіть текст")
    while True:
        print("Виберіть результат виводу\n")
        print("1: Частота літер\n")
        print("2: Частота слів (усі)\n")
        print("3: Частота слів (ті що повторюються)\n")
        print("0: Вихід з програми\n")
        choice = input("Введіть 1, 2, 3, або 0: ").strip()

        if choice == "0":
            print("Завершення роботи програми")
            return
        elif choice not in ["1", "2", "3"]:
            print("Невірний вибір! Спробуйте ще раз.\n")
            continue
        if choice == "1":
            letter_chast = {}
            for chast in text_in_file_lower:
                if chast.isalpha():
                    letter_chast[chast] = letter_chast.get(chast, 0) + 1
            result_data = sorted(letter_chast.items(), key=lambda x: x[1], reverse=True)
            title_in_file = "Частота літер у тексті"
        elif choice == "2":
            word_chast = {}
            for word in all_words:
                word_chast[word] = word_chast.get(word, 0) + 1
            result_data = sorted(word_chast.items(), key=lambda x: x[1], reverse=True)
            title_in_file = "Частота всіх англійських слів у тексті"
        elif choice == "3":
            word_chast = {}
            for word in all_words:
                word_chast[word] = word_chast.get(word, 0) + 1

            filtered = list(filter(lambda x: x[1] >= 2, word_chast.items()))
            result_data = sorted(filtered, key=lambda x: x[1], reverse=True)
            title_in_file = "Частота всіх англійських слів, що зустрічаються більше 2 разів"
        end_time = time.time()
        execution_time = round(end_time - start_time, 3)
        last_modif = datetime.datetime.fromtimestamp(os.path.getmtime(file_name)).strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n{title_in_file}:")
        for item, count in result_data[:20]:
            print(f"{item} - {count} разів")
        with open(result_file, "w", encoding="UTF-8") as outfile:
            outfile.write(f"час створення результату: {start_datetime}\n")
            outfile.write(f"час останніх змін у файлі: {last_modif}\n")
            outfile.write(f"час виконання аналізу: {execution_time}\n")
            outfile.write(f"{title_in_file}\n\n")

            for item, count in result_data:
                outfile.write(f"{item} - {count} разів\n")
        print(f"Час виконання: {execution_time} секунд")


# task1()
# task2()
# task3()
# task4()
# task5()
task6()