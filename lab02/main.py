import random
import math
# print("Завдання 1------")
#
#
# def task1():
#     random_number = random.sample(range(0, 101), 10)
#     print(random_number)
#     print("Числа які <= 50")
#     for i in random_number:
#         if i <= 50:
#             print(i)
#
#
# task1()
# print("Завдання 2------")
#
#
# def task2():
#
#     sum_price = float(input("Введіть суму покупки"))
#
#
#     while sum_price < 0:
#         sum_price = float(input("Введіть суму покупки"))
#         sum_buy = 0
#         if sum_price < 0:
#             print("не може бути  від'ємне число")
#
#     if sum_price < 500:
#         sum_buy = sum_price
#         print("Загальна ціна", sum_buy)
#     elif 500 < sum_price < 1000:
#         action = sum_price * (3 / 100)
#         sum_buy = sum_price - action
#         print("Загальна ціна", sum_buy)
#     elif sum_price > 1000:
#         action = sum_price * (5 / 100)
#         sum_buy = sum_price - action
#         print("Загальна ціна", sum_buy)
#
#
# task2()
# print("Завдання 3------")
#
#
# def task3():
#
#     dov_osn = float(input("Введіть довжину основи: "))
#     while dov_osn <= 0:
#         if dov_osn <= 0:
#             print("не може бути  від'ємне число")
#     dov_stor = float(input("Введіть довжину рівнобедрених сторін: "))
#     while dov_stor <= 0:
#         if dov_stor <= 0:
#             print("не може бути  від'ємне число")
#     piv_per = (dov_osn + 2 * dov_stor) / 2
#     print(piv_per)
#     S = math.sqrt(piv_per * (piv_per - dov_stor) * (piv_per - dov_stor) * (piv_per - dov_osn))
#     print("Площа рівнобедреного трикутника", S)
#     if S % 2 == 0:
#         print("Умова виконується", S / 2)
#     else:
#         print("Не можу поділити на 2")
#
#
# task3()
#
#
# print("Завдання 4")
#
#
# def task4():
#     a = int(input("Введіть число А(А<B)"))
#     b = int(input("Введіть число B"))
#
#     while a > b:
#         if a > b:
#             print("Число В має бути більше")
#
#         b = int(input("Введіть число B"))
#
#     all_num = []
#     sum_all_num = 0
#     for num in range(a, b + 1, 1):
#         all_num.append(num)
#         sum_all_num = sum(all_num)
#     print("Сума чисел від А до В", sum_all_num)
#
#
# task4()
#
# print("Завдання 5")
#
#
# def task5():
#     a = int(input("Введіть число А(А<B)"))
#     b = int(input("Введіть число B"))
#     while a > b:
#         if a > b:
#             print("Число В має бути більше")
#
#         b = int(input("Введіть число B"))
#     all_num = []
#     sum_all_num = 0
#     all_sq = 0
#
#     for num in range(a, b + 1, 1):
#         all_num.append(num)
#
#         all_sq = [sq ** 2 for sq in all_num]
#         print(all_sq)
#         sum_all_num = sum(all_sq)
#     print("Сума квадратів чисел від А до В", sum_all_num)
#
#
# task5()
#
# print("Завдання 6---------")
#
#
# def task6():
#     a = int(input("Введіть число А(А<=B)"))
#     b = int(input("Введіть число B"))
#     while a > b:
#         if a > b:
#             print("Число В має бути більше або дорівнювати А")
#
#         b = int(input("Введіть число B"))
#     all_num = []
#     all_sum = 0
#     while b >= a:
#         all_num.append(a)
#         all_sum = sum(all_num)
#         a += 1
#     print(all_sum)
#
#
# task6()
#
# print("Завдання 7---------")
#
#
# def task7():
#     a = int(input("Введіть значення a"))
#     b = 50
#     while 0 > a or a > 50:
#         if 50 < a or a < 0:
#             print("а не може бути менше 0 або більше 50")
#
#         a = int(input("Введіть значення a"))
#     all_num = []
#     all_sum = 0
#     for num in range(a, 50, 1):
#         all_num.append(num)
#         all_sq = [sq ** 2 for sq in all_num]
#         print(all_sq)
#         all_sum = sum(all_sq)
#         print("Сума квадратів всіх всіх цілих чисел від а до 50",all_sum)
#
#
# task7()
#
#
# print("Завдання 8---------")
#
#
# def task8():
#     n = int(input("Введіть число n: "))
#     while n < 1:
#         if n < 1:
#             print("n має бути більше 1")
#         n = int(input("Введіть число n: "))
#     k = 1
#
#     while 5 ** k < n:
#         k += 1
#         if n < 5:
#             k = 1
#
#     print("Найменше число k", k)
#
#
# task8()
#
#
# print("Завдання 9------------")
#
#
# def task9():
#
#     n = int(input("Введіть число n: "))
#     while n < 1:
#         print("Число не може бути менше 1")
#         n = int(input("Введіть число n: "))
#     arr = 0
#     num_min = 0
#     for num in range(1, 200, 1):
#         arr = [kv ** 2 for kv in range(1, 50000, 1)]
#         arr.append(num)
#         if n < arr[num]:
#             num_min = arr[num]
#             break
#     print("Перше чило більше за n", num_min)
#
#
# task9()
#
#
# print("Завдання 10--------")
#
#
# def task10():
#     n = int(input("Введіть число n: "))
#     while n < 1:
#         print("Число не може бути менше 1")
#         n = int(input("Введіть число n: "))
#     first_el = 1
#     rizn = 1
#     while first_el < n:
#         first_el = first_el + rizn
#         rizn = rizn + 2
#     print("Перше число більше n: ", first_el)
#
#
# task10()
#
# print("Завдання 11------------")
#
#
# def task11():
#
#     m = int(input("Введіть місяць(числом)"))
#     if m < 1 or m > 12:
#         while m < 1 or m > 12:
#             if m < 1 or m > 12:
#                 print("Місяць не може бути менше 1 і більше 12")
#             m = int(input("Введіть місяць(числом)"))
#     d = int(input("Введіть день"))
#     days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if d < 1 or d > days_month[m - 1]:
#         for day in days_month:
#             while d < 1 or d > days_month[m - 1]:
#                 if d < 1 or d > days_month[m - 1]:
#                     print("День не може бути менше 1 і більше 31")
#                 d = int(input("Введіть день"))
#     day_of_year = d + sum(days_month[0: m - 1])
#     start_day = [(20, 1, "Водолій"), (19, 2, "Риби"), (21, 3, "Овен"), (20, 4, "Телець"), (21, 5, "Близнюки"),
#                  (22, 6, "Рак"), (23, 7, "Лев"), (23, 8, "Діва"), (23, 9, "Терези"), (23, 10, "Скорпіон"),
#                  (23, 11, "Стрілець"), (22, 12, "Козеріг")]
#     zodiac = "Козеріг"
#     for day, month, value in start_day:
#         start = day + sum(days_month[:month - 1])
#         if day_of_year >= start:
#             zodiac = value
#
#     print(zodiac)
#
#
# task11()
#
print("Завдання 12---------")


def task12():
    in_kg = [1, 0.000001, 0.001, 1000, 100]
    od = [(1, "кілограм"), (2, "міліграм"), (3, "грам"), (4, "тонна"), (5, "центнер")]
    num_mas = int(input("Номер маси(1 — кілограм, 2 – міліграм, 3 – грам, 4 – тонна, 5 – центнер): "))
    mas_in_od = float(input("Введіть масу в вказаних одиницях"))
    mas_in_kg = 0
    for num, sing in od:
        if num == num_mas:
            mas_in_kg = mas_in_od * in_kg[num - 1]
    print("Маса в кілокграмах: ", mas_in_kg)


task12()
