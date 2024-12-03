import matplotlib.pyplot as plt
import numpy as np

# # Создаём экземпляр класса figure и добавляем к Figure область Axes
# fig, ax = plt.subplots()
# # Добавим заголовок графика
# ax.set_title('График функции')
# # Название оси X:
# ax.set_xlabel('x')
# # Название оси Y:
# ax.set_ylabel('y')
# # Начало и конец изменения значения X, разбитое на 100 точек
# x = np.linspace(-5, 5, 100) # X от -5 до 5
# # Построение прямой
# y = y = 1 / x
# # Вывод графика
# ax.plot(x, y)
# plt.show()


import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([25, 32, 34, 20, 25])
plt.plot(x, y)
plt.xlabel('Ось х')  # Подпись для оси х
plt.ylabel('Ось y')  # Подпись для оси y
plt.xlim(-10, 10)
plt.title('Первый график')  # Название
plt.show()
