a = int(input())
b = int(input())
if b != 0:
    print(a/b)
else:
    print('Делить на ноль нельзя!')

a = int(input())
if a > 20:
    b = a*35/100
    print('Предоставленная скидка:', b)
    print('Итоговая сумма с учётом скидки:', a-b)
else:
    print('Итоговая сумма без скидки:', a)

a = int(input())
if a == 12 or a == 1 or a == 2:
    print('Сейчас зима')
    if a == 12:
        print('А именно Декабрь')
        if a == 1:
            print('А именно Январь')
            if a == 2:
                print('А именно Февраль')
elif a == 3 or a == 4 or a == 5:
    if a == 3:
        print('Сейчас весна')
        print('А именно Март')
    elif a == 4:
        print('Сейчас весна')
        print('А именно Апрель')
    elif a == 5:
        print('Сейчас весна')
        print('А именно Май')
elif a == 6 or a == 7 or a == 8:
    if a == 6:
        print('Сейчас лето')
        print('А именно Июнь')
    elif a == 7:
        print('Сейчас лето')
        print('А именно Июль')
    elif a == 8:
        print('Сейчас лето')
        print('А именно Август')
elif a == 9 or a == 10 or a == 11:
    if a == 9:
        print('Сейчас осень')
        print('А именно Сентябрь')
    elif a == 10:
        print('Сейчас осень')
        print('А именно Октябрь')
    elif a == 11:
        print('Сейчас осень')
        print('А именно Ноябрь')
else:
    if a > 12 or a < 1:
        print('Число введено неверно!')
