
import random
x=random.randint(1,10)
y=random.randint(1,10)
x_1=random.randint (1,10)
y_1=random.randint (1,10)
x_2=random.randint (1,10)
y_2=random.randint (1,10)
print (x,y)
print (x_1,y_1)
print (x_2,y_2)
def less (x,y,x_1,y_1,x_2,y_2):
    return (x/y,x_1/y_1,x_2/y_2)
if x/y<x_1/y_1 and x/y<x_2/y_2:
    print (x,y)
if x_1/y_1<x/y and x_1/y_1<x_2/y_2:
        print (x_1,y_1)
if x_2/y_2<x_1/y_1 and x_2/y_2<x/y:
    print (x_2,y_2)
else:
    print ('не найдено!')
            
