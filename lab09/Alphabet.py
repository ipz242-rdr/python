import re
from string import ascii_uppercase

class Alphabet:
    default_lan = "ua"
    default_let = [
        "А", "Б", "В", "Г", "Ґ", "Д", "Е", "Є", "Ж", "З",
        "И", "І", "Ї", "Й", "К", "Л", "М", "Н", "О",
        "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч",
        "Ш", "Щ", "Ь", "Ю", "Я",
    ]
    ua_language = re.compile(r'^[А-ЯҐЄШЇЙ\']+$', re.IGNORECASE)

    def __init__(self, lang, letters):
        if lang is None:
            self.lang = Alphabet.default_lan
        else:
            self.lang = lang
        if letters is None:
            self.letters = Alphabet.default_let
        else:
            self.letters = letters

    def print_alphabet(self):
        print(" ".join(self.letters).upper())

    def letters_num(self):
        if len(self.letters) == 0:
            print("алфафіт немає літер")
            return
        else:
            print(f"кількість літер в алфавіфті {len(self.letters)}")

    def is_ua_lang(self, text: str) -> bool:
        if not isinstance(text, str):
            return False
        clean_text = re.sub(r'[\d\W]+', '', text)
        if not clean_text:
            return False
        return bool(self.ua_language.fullmatch(clean_text))


class EngAlphabet(Alphabet):
    __en_letters_num = 26
    en_language = re.compile(r'^[A-Z\']+$', re.IGNORECASE)

    def __init__(self):
        super().__init__(lang="EN", letters=list(ascii_uppercase))

    def is_en_letter(self, text: str) -> bool:
        if not isinstance(text, str) or not text.strip():
            return False
        clean_text = re.sub(r'[\d\W]+', '', text)
        if not clean_text:
            return False
        return bool(self.en_language.fullmatch(clean_text))

    def letters_num(self) -> int:
        return self.__en_letters_num

    @staticmethod
    def example() -> str:
        return "I love Python"


ua_alp = Alphabet("UA", "Привіт")
en_alp = Alphabet("UA", "Hello")
print("Літери англійського алфавіту")
en_alp.print_alphabet()
print("Кількість літер")
en_alp.letters_num()
print("Перевірка чи J англійського алфавіту", en_alp.is_ua_lang('J'))
print("Перевірка чи Щ українського алфавіту", ua_alp.is_ua_lang('Щ'))
print(f"Приклад англ тексту {EngAlphabet.example()}")
