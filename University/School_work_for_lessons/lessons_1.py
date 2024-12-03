import math
x = int(input())
t = int(input())
z = ((9*math.pi*t+10*math.cos(x))/math.sqrt(t)-math.fabs(math.sin(t)))*math.e**x
print(z)
