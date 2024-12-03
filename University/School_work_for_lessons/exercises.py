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

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

# Создаем основной класс окна


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Устанавливаем заголовок окна
        self.setWindowTitle("Простое окно PyQt5")
        # Устанавливаем размер и положение окна
        self.setGeometry(100, 100, 800, 600)


def main():
    app = QApplication(sys.argv)  # Создаем экземпляр приложения
    window = MainWindow()  # Создаем экземпляр основного окна
    window.show()  # Показываем окно
    sys.exit(app.exec_())  # Запускаем главный цикл приложения


if __name__ == "__main__":
    main()
