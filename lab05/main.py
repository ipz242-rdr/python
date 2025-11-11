def task1(n, output_format):
    try:
        limit = int(n)
    except ValueError:
        return "Помилка: Верхня межа N має бути числом."
    except TypeError:
        return "Помилка: Верхня межа N має бути числом."

    if limit < 2:
        # Прості числа починаються з 2.
        return f"Помилка: Прості числа шукаються від 2. Задана межа N={limit} занадто мала."
    prime_numbers = []
    for num in range(2, n + 1):
        is_prime = True
        i = 2
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            prime_numbers.append(num)
    if output_format == 'list':
        return prime_numbers
    elif output_format == 'count':
        return len(prime_numbers)
    elif output_format == 'column':
        for p in prime_numbers:
            print(p)
        return
    else:
        return f"Невідомий формат: {output_format}"


task1Test1 = task1(56, 'list')
print(task1Test1)
print('---------')
task1Test2 = task1(20, 'column')
print('---------')
task1Test3 = task1(20, 'count')
print(task1Test3)
print('---------')
