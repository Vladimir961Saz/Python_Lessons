a=int(input())
b=int(input())
if b!=0:
    print (a/b)
else:
    print ('Делить на ноль нельзя!')

a=int(input())
if a>20:
    b=a*35/100
    print ('Предоставленная скидка:',b)
    print ('Итоговая сумма с учётом скидки:',a-b)
else:
    print ('Итоговая сумма без скидки:',a)