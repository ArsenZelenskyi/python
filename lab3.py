
import doctest
import sys


def reverse_words(text: str) -> str:
    """
    Розвертає букви в кожному слові, залишаючи інші символи на місці.

    >>> reverse_words("abcd")
    'dcba'
    >>> reverse_words("abcd efgh")
    'dcba hgfe'
    >>> reverse_words("")
    ''
    >>> reverse_words("a1bcd efg!h")
    'd1cba hgf!e'
    >>> reverse_words(123)
    Traceback (most recent call last):
        ...
    TypeError: Переданий аргумент повинен бути строкою (str).
    """

    if not isinstance(text, str):
        raise TypeError("Переданий аргумент повинен бути строкою (str).")

    if not text.isascii():
        raise ValueError("Текст повинен містити тільки ASCII символи.")

    def reverse_word(word):
        letters = ""

        for char in word:
            if char.isalpha():
                letters += char

        result = ""
        for char in word:
            if char.isalpha():
                result += letters[-1]
                letters = letters[:-1]
            else:
                result += char

        return result

    words = text.split(" ")
    result = []

    for word in words:
        result.append(reverse_word(word))

    return " ".join(result)


def start():
    print("Введіть 'exit' або 'quit' для виходу.\n")

    while True:
        try:
            text = input("Введіть текст: ")

            if text.strip().lower() == "exit" or text.strip().lower() == "quit":
                print("Завершення роботи.")
                break

            answer = reverse_words(text)
            print("Результат:", answer)
            print()

        except ValueError as error:
            print("Помилка введення:", error)
            print()

        except KeyboardInterrupt:
            print("\nПрограму примусово завершено.")
            break

        except Exception as error:
            print("Виникла помилка:", error)
            print()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print("Запуск doctest...")
        failed, total = doctest.testmod()
        print(f"Тестування завершено: {total - failed}/{total} тестів пройдено успішно.")
    else:
        failed, total = doctest.testmod()

        if failed == 0:
            start()
        else:
            print("Виявлено помилки у функціоналі!")
