def caesar(text: str, alphabet: str, step: int, style: str):
    upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

    for i in range(len(text)):

        if alphabet == 'ru':
            alphas = 32
            low_alphabet = lower_rus_alphabet
            up_alphabet = upper_rus_alphabet
        else:
            alphas = 26
            low_alphabet = lower_eng_alphabet
            up_alphabet = upper_eng_alphabet

        if text[i].isalpha():
            if text[i] == text[i].lower():
                place = low_alphabet.index(text[i])
            else:
                place = up_alphabet.index(text[i])

            if style == 'шифровать':
                index = (place + int(step)) % alphas
            else:
                index = (place - int(step)) % alphas

            if text[i].islower():
                print(low_alphabet[index], end='')
            else:
                print(up_alphabet[index], end='')
        else:
            print(text[i], end='')


def main():
    what_alphabet = input("Введи язык - 'ru' или 'en': ")
    while what_alphabet.lower() != 'ru' and what_alphabet.lower() != 'en':
        what_alphabet = input("Что-то не то ты ввел. Введи 'ru' или 'en': ")

    what_text = input("Введи текст: ")
    while what_text.isspace():
        what_text = input("Что-то не то ты ввел. Введи текст: ")

    what_step = input("Введи шаг: ")
    while not what_step.isdigit():
        what_step = input("Что-то не то ты ввел. Введи число: ")

    what_style = input("Введите стиль, шифровать или дешифровать: ")
    while what_style != 'шифровать' and what_style != 'дешифровать':
        what_style = input("Ты ввел что-то не то. Введи шифровать или дешифровать: ")

    caesar(what_text, what_alphabet, what_step, what_style)


if __name__ == '__main__':
    main()
