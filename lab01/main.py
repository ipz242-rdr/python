def numerics():
    function1 = float(input("Введіть число 1:"))
    function2 = float(input("Введіть число 2:"))
    function3 = float(input("Введіть число 3:"))
    function4 = float(input("Введіть число 4:"))
    return function1, function2, function3, function4


def operations(numbers):
    operation = []

    summa = sum(numbers)
    operation.append(summa)
    dob = numbers[0] * numbers[1] * numbers[2] * numbers[3]
    operation.append(dob)

    if numbers[0] == 0 or numbers[1] == 0 or numbers[2] == 0 or numbers[3] == 0:
        print("Помилка")
    else:
        dil = numbers[0] / numbers[1] / numbers[2] / numbers[3]
        operation.append(dil)

    step = numbers[0] ** numbers[1]
    operation.append(step)


    if numbers[0] == 0 or numbers[1] == 0 or numbers[2] == 0 or numbers[3] == 0:
        print("Помилка")
    else:
        dilNac = numbers[0] // numbers[1] // numbers[2] // numbers[3]
        operation.append(dilNac)

    ostacha = numbers[0] % numbers[1]
    operation.append(ostacha)
    print(operation)
    evenEl = []
    for num in operation:
        if num % 2 == 0:
            evenEl.append(num)

    print("Кількість парних елементів", evenEl)
    newList = operation
    temp = operation[1]
    if operation[4] == 0:
        operation[4] = 0

    operation[1] = operation[4]
    operation[4] = temp
    newList.append(operation[1])
    newList.append(operation[4])
    print("Зміна 2 та 5 елементу", newList)


operations(numerics())

name = input("Введіть Прізвище та ім'я: ")
print(name)
print("Висновки: В даній лаболаторній роботі я навчивсь створювати змінні, отримувати значення від користувача. \n"
      "Навчивсь працювати з операціями\n"
      "Також розібравсь зі списком та навчивсь працювати з індексами")

