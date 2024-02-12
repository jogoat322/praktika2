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
        else:
            morse_code += '/ '  # Use '/' to represent space
    return morse_code

def morse_to_text(morse_code):
    morse_code = morse_code.split(' ')
    text = ''
    for code in morse_code:
        for key, value in MORSE_CODE_DICT.items():
            if code == value:
                text += key
    return text

if __name__ == "__main__":
    message = input("Введите текст для кодирования/декодирования: ")

    choice = input("Выберите операцию (1 - Кодирование, 2 - Декодирование): ")

    if choice == '1':
        result = text_to_morse(message)
        print(f"Результат кодирования: {result}")
    elif choice == '2':
        result = morse_to_text(message)
        print(f"Результат декодирования: {result}")
    else:
        print("Некорректный выбор операции. Выберите 1 или 2.")
