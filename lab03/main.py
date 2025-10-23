import re


text = input("Введіть текст")


# Task 1
def task1():

    good = False
    if text == "":
        print("Ви нічого не ввели")
        return
    if re.fullmatch(r"[А-Яа-яІіЇїЄєҐґ.?,\-=+:;!'\"\s]+", text):
        words = text.split()
        if len(words) > 1000:
            print("Забагато слів")
            return
        currentWord = input("Введіть слово яке хочете знайти: ")
        while not good:
            if currentWord == "":
                print("Ви нічого не ввели")
                good = False
                currentWord = input("Введіть слово яке хочете знайти: ")
            else:
                good = True
        words = text.split()

        if currentWord in words:
            index = words.index(currentWord)
            words_after = words[index + 1:]
            count_after = len(words_after)
            print("Кількість слів після слова введеного користувачем: ", count_after)
        else:
            print("Такаго слова немає")
    else:
        print("Текст не український, або не зрозумілі розділові знаки")
        return


# Task 2
def task2():
    if text == "":
        print("Ви нічого не ввели")
        return
    if re.fullmatch(r"[А-Яа-яІіЇїЄєҐґ.?,\-=+:;!'\"\s]+", text):
        number_caps_letter = text.count("а")
        letters_a = text.replace("а", "А")
        print("Змінений рядок:" + letters_a)
        print("Кількість замін:", number_caps_letter)
        length_letters = letters_a.replace(" ", "")
        print(len(length_letters))
    else:
        print("Текст не український")
        return


# Task 3
def task3():
    if text == "":
        print("Ви нічого не ввели")
        return
    good = False
    number_current_word = 0
    if re.fullmatch(r"[А-Яа-яІіЇїЄєҐґ.?,\-=+:;!'\"\s]+", text):
        current_word = input("Введість слово яке хочете знайти")
        while not good:
            if current_word == "":
                print("Ви нічого не ввели")
                good = False
                current_word = input("Введіть слово яке хочете знайти: ")
            else:
                good = True
        clean_test = re.sub(r"[^А-Яа-яІіЇїЄєҐґ\s]+", "", text)
        words = clean_test.split()
        for word in words:

            if word.lower() == current_word.lower():
                number_current_word += 1
        print(number_current_word)
    else:
        print("Текст не український, або не зрозумілі розділові знаки")
        return


def task4():
    if text == "":
        print("Ви нічого не ввели")
        return
    if re.fullmatch(r"[А-Яа-яІіЇїЄєҐґ.?,\-=+:;!'\"\s]+", text):
        mid = len(text) // 2
        medium_text_rev = text[:mid]
        medium_text_after = text[mid:]
        words_medium_text_rev = ''
        new_text = ''
        if medium_text_rev:
            words_medium_text_rev = medium_text_rev.title()
        else:
            print("ваш рядок замалий")
            return
        if medium_text_after:
            split_after_mid_text = medium_text_after.split()
            words_medium_text_after = ' *'.join(split_after_mid_text)
            new_text = words_medium_text_rev + ' | *' + words_medium_text_after.lower()
        print(new_text)
    else:
        print("Текст не український, або не зрозумілі розділові знаки")
        return


def task5():
    if text == "":
        print("Ви нічого не ввели")
        return
    if re.fullmatch(r"[A-Za-z.?,\-=+:;!'\"\s]+", text):
        words = text.split()
        if len(words) > 3000:
            print("Забагато слів")
            return
        cleans_text = re.sub(r"[^A-Za-z\s]+", "", text)
        split_clean_text = cleans_text.split()
        leter_n = 'n'
        leter_p = 'p'
        selected_n = [clean_text for clean_text in split_clean_text
                    if clean_text.lower().startswith(leter_n.lower())]

        selected_p = [clean_text for clean_text in split_clean_text
                      if clean_text.lower().startswith(leter_p.lower())]
        all_text = selected_n + selected_p
        if not all_text:
            print("В тексті немає слів що починаються на N та P")
        else:
            print(all_text)
    else:
        print("Текст не англійський, або не зрозумілі розділові знаки")
        return


def task6():
    if text == "":
        print("Ви нічого не ввели")
        return
    if re.fullmatch(r"[A-Za-z.?,\-=+:;!'\" 0-9\s]+", text):
        words = text.split()
        if len(words) > 100:
            print("Забагато слів")
            return
        lower_text = text.lower()
        gol_letter = 0
        gol = "ayuioe"
        gol_letter = sum(1 for ch in lower_text if ch in gol)
        print("Кількість голосних літер: ", gol_letter)
    else:
        print("Текст не англійський, або не зрозумілі розділові знаки")
        return


def task7():
    if text == "":
        print("Ви нічого не ввели")
        return
    if re.fullmatch(r"[A-Za-z.?,\-=+:;!'\" 0-9\s]+", text):
        words = text.split()
        if len(words) > 1000:
            print("Забагато слів")
            return
        cleans_text = re.sub(r"[^A-Za-z\s]+", "", text)
        split_clean_text = cleans_text.split()
        upper_words = []

        for upper_letter in split_clean_text:
            if upper_letter[0].isupper():
                upper_words.append(upper_letter)
        if upper_words:
            print("Слова з великої літери: ", upper_words)
        else:
            print("Немає слів з великої літери")
            return
    else:
        print("Текст не англійський, або не зрозумілі розділові знаки")
        return


# task1()
task2()
# task3()
# task4()
# task5()
# task6()
# task7()
