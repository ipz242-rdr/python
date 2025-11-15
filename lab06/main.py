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


task1()

