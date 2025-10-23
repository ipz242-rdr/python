import random


def task1():
    my_list = []
    num = 0
    max_num = 0
    good = False
    while not good:
        try:
            num = int(input("Введіть скільки чисел буде в списку"))
            if num < 0:
                good = False
                print("Ви ввели від'ємне число")
            else:
                good = True
        except ValueError:
            print("Ви ввели не число")
    for enter_my_list in range(num):
        try:
            enter_my_list = int(input("Введіть числа (тільки цілочисельні)"))
            my_list.append(enter_my_list)
            max_num = max(my_list)
        except ValueError:
            print("Ви ввели не ціле число")
    my_list.reverse()
    print(my_list)
    print("Найбільше число: ", max_num)


def task2():
    my_list = []
    positive_num = []
    another_num = []
    count = 0
    good = False
    while not good:
        try:
            count = int(input("Введіть скільки чисел буде в списку"))
            if count < 0:
                good = False
                print("Ви ввели від'ємне число")
            else:
                good = True
        except ValueError:
            print("Ви ввели не число")
    for enter_my_list in range(count):
        try:
            enter_my_list = int(input("Введіть числа (тільки цілочисельні)"))
            my_list.append(enter_my_list)
            if enter_my_list > 0:
                positive_num.append(enter_my_list)
            else:
                another_num.append(enter_my_list)
        except ValueError:
            print("Ви ввели не ціле число")
    print("Весь список: ", my_list)
    print("Додатні числа: ", positive_num)
    print("Список без додатніх чисел: ", another_num)


def task3():
    my_list = [random.randint(-10, 10) for _ in range(20)]
    sum_odd_list = 0
    print(my_list)
    for i in range(0, len(my_list), 2):
        sum_odd_list += my_list[i]
    print(sum_odd_list)


def task4():
    my_list = [random.randint(-100, 100) for _ in range(30)]
    another_list = []
    max_num = max(my_list)
    max_num_index = my_list.index(max_num)
    print(my_list)
    print(f"Максимальне значення {max_num} а його індекс {max_num_index + 1}")
    for i in range(len(my_list)):
        if my_list[i] % 2 == 1:
            another_list.append(my_list[i])
    if not another_list:
        print("непарних чисел немає")
    else:
        another_list.sort(reverse=True)
        print("Список непарних чисел", another_list)


def task5():
    my_list = [random.randint(-100, 100) for _ in range(30)]
    odd_negative_list = []
    for i in range(len(my_list) - 1):
        if my_list[i] < 0 and my_list[i + 1] < 0:
            odd_negative_list.append(f"({my_list[i]}; {my_list[i + 1]})")
    print(my_list)
    print(odd_negative_list)


def task6():
    my_list = [random.randint(-10, 10) for _ in range(10)]
    max_num = max(my_list)
    sq_num_list = []
    for i in range(len(my_list)):
        if my_list[i] < max_num:
            sq_num_list.append(my_list[i] * my_list[i])

        else:
            max_num = my_list[i]
    print(my_list)
    print(max_num)
    sq_num_list.sort(reverse=True)
    print(sq_num_list)


def task7():
    my_list = []
    abs_list = []
    min_num_abs = 0
    for _ in range(30):
        if random.choice([True, False]):
            my_list.append(random.randint(-100, 100))
        else:
            my_list.append(round(random.uniform(-100, 100), 2))
    for i in range(len(my_list)):
        abs_list.append(abs(my_list[i]))
        min_num_abs = min(abs_list)
    print(my_list)
    my_list.sort()
    abs_list.sort()
    print(min_num_abs)
    print("Список по модулю", abs_list)
    print("Ввесь список", my_list)


def task8():
    my_list = []
    matrix = []
    matrix_sorted = []
    row = []
    sorted_matrix = []
    for _ in range(30):
        if random.choice([True, False]):
            my_list.append(random.randint(-100, 100))
        else:
            my_list.append(round(random.uniform(-100, 100), 2))
    for i in range(0, len(my_list), 3):
        row = my_list[i:i+3]
        matrix.append(row)
        sorted_matrix = sorted(matrix, key=lambda row: sum(abs(x) for x in row))
    print(matrix)
    print(sorted_matrix)


# task1()
# task2()
# task3()
# task4()
# task5()
# task6()
# task7()
task8()
