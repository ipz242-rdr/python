class NameLengthError(ValueError):

    def __init__(self, name: str, min_length: int = 10):
        message = (
            f"Помилка довжини імені: Довжина імені '{name}' "
            f"становить {len(name)}, що менше мінімальної необхідної довжини {min_length}."
        )
        super().__init__(message)
        self.name = name
        self.min_length = min_length


def validate_name(name: str):

    min_length = 10

    if len(name) < min_length:
        raise NameLengthError(name, min_length)

    return f"Ім'я '{name}' успішно пройшло перевірку."


if __name__ == "__main__":

    name_ok = "Володимир_Зоря"
    name_short = "Наталія"

    print(" Успішна перевірка")
    try:
        print(validate_name(name_ok))
    except NameLengthError as e:
        print(f"Помилка: {e}")

    print(" Невдала перевірка")
    try:
        validate_name(name_short)
        print("Перевірка успішна")
    except NameLengthError as e:
        print(f"Згенеровано виняток:")
        print(e)
