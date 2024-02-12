import os

MORSE_CODE_DICT = {'А': '.-', 'Б': '-...',
                  'В': '.--', 'Г': '--.', 'Д': '-..',
                  'Е': '.', 'Ё': '.', 'Ж': '...-', 'З': '--..',
                  'И': '..', 'Й': '.---', 'К': '-.-',
                  'Л': '.-..', 'М': '--', 'Н': '-.',
                  'О': '---', 'П': '.--.', 'Р': '.-.',
                  'С': '...', 'Т': '-', 'У': '..-',
                  'Ф': '..-.', 'Х': '....', 'Ц': '-.-.',
                  'Ч': '---.', 'Ш': '----', 'Щ': '--.-',
                  'Ъ': '-..-', 'Ы': '-.--', 'Ь': '-..-',
                  'Э': '..-..', 'Ю': '..--', 'Я': '.-.-',
                  '1': '.----', '2': '..---', '3': '...--',
                  '4': '....-', '5': '.....', '6': '-....',
                  '7': '--...', '8': '---..', '9': '----.',
                  '0': '-----', ', ': '--..--', '.': '.-.-.-',
                  '?': '..--..', '/': '-..-.', '-': '-....-',
                  '(': '-.--.', ')': '-.--.-', ' ': '/'}

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        elif char == ' ':
            morse_code += '\t' 
        else:
            morse_code += '/ '  
    return morse_code

def morse_to_text(morse_code):
    morse_code = morse_code.split(' ')
    text = ''
    for code in morse_code:
        for key, value in MORSE_CODE_DICT.items():
            if code == value:
                text += key
        if code == '\t':
            text += ' ' 
    return text

def save_to_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)

def main():
    while True:
        print("Выберите действие:")
        print("1. Кодирование текста в азбуку Морзе")
        print("2. Декодирование азбуки Морзе в текст")
        print("3. Завершить программу")

        choice = input("Введите номер действия: ")

        if choice == '1':
            text = input("Введите текст для кодирования: ")
            morse_code = text_to_morse(text)
            print(f"Результат кодирования: {morse_code}")
            save_choice = input("Сохранить результат в файл? (y/n): ")
            if save_choice.lower() == 'y':
                filename = input("Введите имя файла для сохранения: ")
                save_to_file(filename, morse_code)
        elif choice == '2':
            morse_code = input("Введите азбуку Морзе для декодирования: ")
            text = morse_to_text(morse_code)
            print(f"Результат декодирования: {text}")
            save_choice = input("Сохранить результат в файл? (y/n): ")
            if save_choice.lower() == 'y':
                filename = input("Введите имя файла для сохранения: ")
                save_to_file(filename, text)
        elif choice == '3':
            print("Программа завершена.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, введите 1, 2 или 3.")

if __name__ == "__main__":
    main()
