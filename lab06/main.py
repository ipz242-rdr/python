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


# task1()
task2()

