# 1
import os


def read_last(enter_file: str = 'article.txt', use_lines: int = 0):
    try:
        with open(f'{enter_file}', 'r', encoding="utf-8") as use_file:
            data_list = use_file.readlines()

        if 0 <= use_lines <= len(data_list):
            for i in range(1, use_lines + 1):
                print(data_list[-i], end="")
        else:
            print("Введите допустимые значения строк,между null и count строками файла")

    except FileNotFoundError as traceback:
        print(f"File not found. Traceback: {traceback}")


lines = int(input('Введите строки: '))
file = input('Введите файл article.txt: ')
read_last(use_lines=lines, enter_file=file)


# 2


def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит:')
        print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
        print(f'Файлы: {", ".join([file for file in catalog[2]])}')
        print('-' * 40)


print_docs('C:/Users/User/Downloads/')


# 3

def longest_words(file):
    with open(file, "r") as text:
        words = text.read().split()

    max_length = len(max(words, key=len))
    sought_words = [word for word in words if len(word) == max_length]

    f = "result.txt"
    i = 1
    while os.path.exists(f):
        f = f"result{i}.txt"
        i += 1
    with open(f, 'w') as file:
        file.write(' '.join(sought_words) + "\n")


longest_words('article.txt')

# 4


def text_editor():
    file_name = input("Введите имя файла (без расширения): ") + ".txt"

    with open(file_name, "w") as file:
        print(f"Файл {file_name} открыт для редактирования.")
        print("Введите текст (для завершения введите пустую строку).")

        while True:

            line = input()

            if line == "" or line in ["@", "#", "$"]:
                print(f"Сохранение файла {file_name} и завершение работы.")
                break

            file.write(line + "\n")


text_editor()
