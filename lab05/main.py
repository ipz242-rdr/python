def find_primes(n, output_format):
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


def analyze_nested_categories(data):
    unique_categories = set()
    total_sums = {}

    def process_element(element):
        if isinstance(element, list):
            for item in element:
                process_element(item)
        elif isinstance(element, dict):
            for category, amount in element.items():
                unique_categories.add(category)

                total_sums[category] = total_sums.get(category, 0) + amount
        pass
    process_element(data)
    return (list(unique_categories), total_sums)


task1Test1 = find_primes(56, 'list')
print(task1Test1)
print('---------')
task1Test2 = find_primes(20, 'column')
print('---------')
task1Test3 = find_primes(20, 'count')
print(task1Test3)
print('---------')


nested_data = [
    [{"офіс": 100}, {"маркетинг": 200}],
    [
        [{"офіс": 50}, {"маркетинг": 150}],
        {"офіс": 200}
    ],
    {"офіс": 300},
    [{"офіс": 100, "extra": 1}]
]
result = analyze_nested_categories(nested_data)
print(f"Результат: {result}")


