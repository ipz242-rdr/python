import re


class DecimalToRoman:
    roman_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
    ]

    def convert(self, number):
        if not isinstance(number, int):
            raise ValueError("Помилка введіть ціле число")
        if number <= 0 or number >= 4000:
            raise ValueError("Помилка число мажє бути в діапазоні 1-3999")

        result = ""
        for arabic, roman in self.roman_map:
            while number >= arabic:
                result += roman
                number -= arabic

        return result


class RomanToDecimal:
    roman_values = {
        "M":1000, "D":500, "C":100, "L":50,
        "X":10, "V":5, "I":1
    }

    @staticmethod
    def validate(roman: str):
        valid_chars = "IVXLCDM"
        for ch in roman:
            if ch not in valid_chars:
                raise ValueError("Некоректні символи у римську числі")
        if re.search(r"(IIII|XXXX|CCCC|MMMM)", roman):
            raise ValueError("Некоректний формат занадто багато повторів")

        invalid_subtrac = ["IL", "IC", "ID", "IM", "VL", "VC", "VD", "VM", "XD",
                           "XM", "VV", "LL", "DD", "IIX", "IIV", "XXC", "XXL"]

        for item in invalid_subtrac:
            if item in roman:
                raise ValueError("Некоректне використання віднімальних символів")

    def convert(self, roman):
        if not isinstance(roman, str):
            raise ValueError("Помилка введіть рядок")

        roman = roman.upper()

        for char in roman:
            if char not in self.roman_values:
                raise ValueError(f"Помилка незрозумілий символ '{char}' у римському числі")

        RomanToDecimal.validate(roman)

        result = 0
        prev_value = 0

        for char in reversed(roman):
            value = self.roman_values[char]
            if value < prev_value:
                result -= value
            else:
                result += value
                prev_value = value

        return result


def task07():
    print(DecimalToRoman().convert(1987))
    print(DecimalToRoman().convert(157))
    print(RomanToDecimal().convert("IV"))
    print(RomanToDecimal().convert("XL"))
    print(RomanToDecimal().convert("VIII"))


task07()
