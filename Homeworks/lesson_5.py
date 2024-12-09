# 1
import random
x = random.randint(1, 10)
y = random.randint(1, 10)
x_1 = random.randint(1, 10)
y_1 = random.randint(1, 10)
x_2 = random.randint(1, 10)
y_2 = random.randint(1, 10)
print(x, y)
print(x_1, y_1)
print(x_2, y_2)


def less(x, y, x_1, y_1, x_2, y_2):
    return (x/y, x_1/y_1, x_2/y_2)


if y/x < y_1/x_1 and y/x < y_2/x_2:
    print(x, y)
    if y_1/x_1 < y/x and y_1/x_1 < y_2/x_2:
        print(x_1, y_1)
        if y_2/x_2 < y_1/x_1 and y_2/x_2 < y/x:
            print(y_2, x_2)
else:
    print('не найдено!')

# 2
print('\n#2')


def p(n):
    s = bin(n)[2:]
    s1 = s[:(len(s))//2]
    s2 = s[(len(s)-1)//2+1:]
    return s1[::-1] == s2


def f(n):
    v = n
    d = 2
    if n == 1:
        return False
    else:
        while d <= n//2:
            if n % d == 0:
                v = 0
            d += 1
        if v == 0:
            return False
        else:
            return p(v)


n = int(input('Введите n: '))
m = []
for i in range(0, n+1):
    if f(i) == True:
        m.append(i)
print(m)
