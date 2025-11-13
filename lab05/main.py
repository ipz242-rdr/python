from datetime import datetime
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

def analyze_clients(clients):
    def valid_email(email):
        return bool(email) and email.count('@') == 1
    results = {
        "status_count": {},
        "invalid_emails": [],
        "new_clients": [],
        "errors": [],
    }

    for item in clients:
        is_valid_client = True
        if not isinstance(item, tuple) or len(item) != 3:
            results["errors"].append(item)
            continue
        name, status, email = item
        if not all(isinstance(field, str) for field in [name, status, email]):
            results["errors"].append(item)
            continue
        if not name:
            is_valid_client = False
        if not status:
            is_valid_client = False
        if not valid_email(email):
            results["invalid_emails"].append(email)
            is_valid_client = False
        if is_valid_client:
            results["status_count"][status] = results["status_count"].get(status, 0) + 1
            if status == "новий":
                results["new_clients"].append(name)
        else:
            results["errors"].append(item)
    return results

test_data = [
    ("Іван", "новий", "ivan@email.com"),
    ("Олена", "постійний", "olena[at]mail.com"),
    ("", "новий", "ivan@email.com"), # некоректне ім'я
    ("Олена", "", "olena@mail.com"), # некоректний статус
    ("Іван", "новий", ""), # некоректний email
    ("", "", ""), # два некоректних поля
    ("Петро", "", ""), # некоректний статус та email
    "не кортеж", # невірний формат даних
    123, # невірний формат даних
    None, # невірний формат даних
    ("Олена",), # невірний формат всередині кортежу (довжина 1)
    ("Іван", "новий"), # невірний формат всередині кортежу (довжина 2)
    (123, "новий", "ivan@email.com"), # невірний тип для імені
    ("Іван", 123, "ivan@email.com"), # невірний тип для статусу
    ("Іван", "новий", 123), # невірний тип для email
    ("Дмитро", "новий", "dmytrorudenko061@gmail.com")
]

final_resultTask3 = analyze_clients(test_data)


def is_valid_date(date_str, date_format="%Y-%m_%d"):
    try:
        datetime.strptime(date_str, date_format)
        return True
    except (ValueError, TypeError):
        return False

def analyze_expenses(expenses):
    category_totals = {}
    invalid_dates = []
    errors = []
    valid_expenses = []
    for expense in expenses:
        if not isinstance(expense, tuple) or len(expense) != 3:
            errors.append(expense)
            continue
        amount, category, date = expense

        if not isinstance(amount, (int, float)) or amount is None:
            errors.append(expense)
            continue
        if not isinstance(category, str) or not category:
            errors.append(expense)
            continue
        if not isinstance(date, str) or date is None:
            errors.append(expense)
            continue
        if not is_valid_date(date):
            if date not in invalid_dates:
                invalid_dates.append(date)

        current_total_cat = category_totals.get(category, 0)
        category_totals[category] = current_total_cat + amount
        valid_expenses.append(expense)

    max_expense = max(valid_expenses, key=lambda x: x[0]) if valid_expenses else None

    result = {
        "category_totals": category_totals,
        "max_expense": max_expense,
        "invalid_dates": invalid_dates,
        "errors": errors
    }
    return result

resultTask4 = analyze_expenses([
(100, "офіс", "2024-06-01"),
(200, "маркетинг", "2024-06-02"),
(50, "офіс", "2024-13-01"),
(None, "маркетинг", "2024-06-02"), # некоректна сума
(100, None, "2024-06-01"), # некоректна категорія
(100, "офіс", None), # некоректна дата
"не кортеж", # невірний формат даних
123, # невірний формат даних
None, # невірний формат даних
(100, "офіс"), # невірний формат всередині кортежу
(100,), # невірний формат всередині кортежу
(100, "офіс", "2024-06-01", "extra") # зайвий елемент у кортежі
])

def filter_reports(reports, output_format, keyword):
    filtered_reports = []
    errors = []

    for report in reports:
        if not isinstance(report, tuple) or len(report) != 3:
            errors.append(report)
            continue
        title = report[0]
        author = report[1]
        format_file = report[2]

        if not all(isinstance(x, str) for x in (title, author, format_file)):
            errors.append(report)
            continue

        if not title or not author or not format_file:
            errors.append(report)
            continue

        if format_file.lower() == output_format.lower() and keyword.lower() in (title + author).lower():
            filtered_reports.append(report)

    return (filtered_reports, len(filtered_reports), errors)


resultTask5 = filter_reports(
[
("Звіт1", "Іван Іванов", "pdf"),
("Звіт2", "Олена Петрівна", "docx"),
("", "Іван Іванов", "pdf"), # некоректна назва
("Звіт3", "", "pdf"), # некоректний автор
("Звіт4", "Петро Сидоров", ""), # некоректний формат
"не кортеж", # невірний формат даних
123, # невірний формат даних
None, # невірний формат даних
("Звіт5",), # невірний формат всередині кортежу
("Звіт6", "Іван Іванов"), # невірний формат всередині кортежу
("Звіт7", "Іван Іванов", 123), # невірний тип для формату
],
"pdf",
"Іва"
)

# task1Test1 = find_primes(56, 'list')
# print(task1Test1)
# print('---------')
# task1Test2 = find_primes(20, 'column')
# print('---------')
# task1Test3 = find_primes(20, 'count')
# print(task1Test3)
# print('---------')


nested_data = [
    [{"офіс": 100}, {"маркетинг": 200}],
    [
        [{"офіс": 50}, {"маркетинг": 150}],
        {"офіс": 200}
    ],
    {"офіс": 300},
    [{"офіс": 100, "extra": 1}]
]
resultTask2 = analyze_nested_categories(nested_data)
# print(f"Результат: {resultTask2}")

# print(final_resultTask3)
# print(resultTask4)
print(resultTask5)

