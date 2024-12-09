# 1
import math
c = 10
x = 10
y = 50
print("до замены x=", x)
print("до замены y=", y)
x = y
y = c
print("после замены x=", x)
print("после замены y=", y)

# 2
L = input("Введите длину маятника: ")
g = 9.81
T = 2*math.pi*math.sqrt(float(L)/g)
print("Проводим некоторые расчёты...")
print("Период колебаний равен:", round(T, 2))

# 3
R = input("Введите радиус окружности в сантиметрах\n")
L = (2*math.pi*float(R))
print(str(L))
