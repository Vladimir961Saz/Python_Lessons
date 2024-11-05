# def read_last(enter_file: str = 'article.txt', use_lines: int = 0):
#     try:
#         with open(f'{enter_file}', 'r', encoding="utf-8") as use_file:
#             data_list = use_file.readlines()


#         if 0 <= use_lines <= len(data_list):
#             for i in range(1, use_lines + 1):
#                 print(data_list[-i], end="")
#         else:
#             print("Введите допустимые значения строк,между null и count строками файла")


#     except FileNotFoundError as traceback:
#         print(f"File not found. Traceback: {traceback}")


# lines = int(input('Введите строки: '))
# file = input('Введите файл article.txt: ')
# read_last(use_lines=lines, enter_file=file)


import os
 
def print_docs(directory):
	all_files = os.walk(directory)
	for catalog in all_files:
          print(f'Папка {catalog[0]} содержит:')
print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
print(f'Файлы: {", ".join([file for file in catalog[2]])}')
print('-' * 40)