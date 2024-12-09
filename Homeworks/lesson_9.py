# 1
import numpy as np
import os
from matplotlib import pyplot as plt
print('\n#1')


dir = os.getcwd()
x = np.linspace(-2, 2, 1000)

plt.rcParams["figure.figsize"] = [5, 5]
plt.rcParams["figure.autolayout"] = True


def f(x, a, b):
    y = (x**b+a**b)/x**b
    y[y > 20] = np.nan
    y[y < -20] = np.nan
    return y


plt.plot(x, f(x, a=1, b=1), label='a=1,b=1', color='black')
plt.plot(x, f(x, a=2, b=1), label='a=2,b=1', color='violet')
plt.plot(x, f(x, a=1, b=2), label='a=1,b=2', color='blue')
ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.title('f(x)=(x^b+a^b)/x^b')
plt.legend()
plt.grid()
plt.savefig(dir + '/Graph_1_lesson_9', dpi=300)
plt.show()

# 2
print('\n#2')


dir = os.getcwd()
x = np.linspace(0, 5, 1000)

plt.rcParams["figure.figsize"] = [5, 5]
plt.rcParams["figure.autolayout"] = True


def f(x, a, b):
    y = (x**b+a**b)/x**b
    y[y > 20] = np.nan
    y[y < -20] = np.nan
    return y


plt.plot(x, f(x, a=1, b=1), label='a=1,b=1', color='black')
plt.plot(x, f(x, a=2, b=1), label='a=2,b=1', color='violet')
plt.plot(x, f(x, a=1, b=2), label='a=1,b=2', color='blue')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('f(x)=(x^b+a^b)/x^b')
plt.legend()
plt.grid()

plt.axes([0.35, 0.60, 0.25, 0.25])
x = np.linspace(0, 0.5, 1000)
plt.grid()
plt.title('Для малых x')
plt.plot(x, f(x, a=1, b=1), label='a=1,b=1', color='black')
plt.plot(x, f(x, a=2, b=1), label='a=2,b=1', color='violet')
plt.plot(x, f(x, a=1, b=2), label='a=1,b=2', color='blue')

plt.axes([0.70, 0.30, 0.25, 0.25])
x = np.linspace(10, 20, 1000)
plt.grid()
plt.title('Для больших x')
plt.plot(x, f(x, a=1, b=1), label='a=1,b=1', color='black')
plt.plot(x, f(x, a=2, b=1), label='a=2,b=1', color='violet')
plt.plot(x, f(x, a=1, b=2), label='a=1,b=2', color='blue')

plt.savefig(dir + '/Graph_2_lesson_9', dpi=300)
plt.show()

# 3
print('\n#3')


dir = os.getcwd()
x = np.linspace(-5, 0, 1000)

plt.rcParams["figure.figsize"] = [5, 5]
plt.rcParams["figure.autolayout"] = True


def f(x, a, b):
    y = (x**b+a**b)/x**b
    y[y > 20] = np.nan
    y[y < -20] = np.nan
    return y


plt.plot(x, f(x, a=1, b=1), label='a=1,b=1', color='black')
plt.plot(x, f(x, a=2, b=1), label='a=2,b=1', color='violet')
plt.plot(x, f(x, a=1, b=2), label='a=1,b=2', color='blue')
plt.plot(x, [0]*len(x), label='f(x)=0', color='black')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('f(x)=(x^b+a^b)/x^b')
plt.legend()
plt.grid()

plt.axes([0.21, 0.17, 0.50, 0.25])


def f(x, a, b):
    y = (x**b+a**b)/x**b
    y[y > 3] = np.nan
    y[y < -3] = np.nan
    return y


x = np.linspace(-5, 0, 1000)
plt.grid()
plt.plot(x, f(x, a=1, b=1), label='a=1,b=1', color='black')
plt.plot(x, f(x, a=2, b=1), label='a=2,b=1', color='violet')
plt.plot(x, f(x, a=1, b=2), label='a=1,b=2', color='blue')
plt.plot(x, [0]*len(x), label='x=0', color='black')

plt.savefig(dir + '/Graph_3_lesson_9', dpi=300)
plt.show()

# 4
print('\n#4')


dir = os.getcwd()
x = np.linspace(-5, 5, 1000)

plt.rcParams["figure.figsize"] = [5, 5]
plt.rcParams["figure.autolayout"] = True


def f(x, a, b):
    y = (x**b+a**b)/x**b
    y[y > 20] = np.nan
    y[y < -20] = np.nan
    return y


plt.plot(x, f(x, a=1, b=0.5), label='a=1,b=0.5', color='black')
plt.plot(x, f(x, a=1, b=-0.5), label='a=1,b=-0.5', color='violet')
plt.plot(x, f(x, a=1, b=-1.5), label='a=1,b=-1.5', color='blue')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('f(x)=(x^b+a^b)/x^b')
plt.legend()
plt.grid()
x = np.linspace(-1, 2, 1000)
plt.savefig(dir + '/Graph_4-1_lesson_9', dpi=300)
plt.show()


def example_plot(ax, x, a, b1, b2, array_b, k, fontsize=12, hide_labels=False):
    ax.plot(x, f(x, a, b1), label=f'a={a},b={b1}', color='red')
    ax.plot(x, f(x, a, b2), label=f'a={a},b={b1}', color='blue')
    ax.grid()
    ax.plot(x, f(x, a, array_b[k][0]),
            label=f'a={a},b={array_b[k][0]}', color='green')
    ax.plot(x, f(x, a, array_b[k][1]),
            label=f'a={a},b={array_b[k][0]}', color='indianred')
    ax.legend()
    ax.locator_params(nbins=3)
    if hide_labels:
        ax.set_xticklabels([])
        ax.set_yticklabels([])
    else:
        ax.set_xlabel('Ось X', fontsize=fontsize)
        ax.set_ylabel('Ось Y', fontsize=fontsize)


fig, axs = plt.subplots(1, 3, figsize=(15, 6))
a = 1
b1 = 0
b2 = -1
array_b = [[0.5, 0.8], [-0.5, -0.8], [-1.5, -2.5]]
k = 0
for ax in axs.flat:
    example_plot(ax, x, a, b1, b2, array_b, k)
    k += 1

plt.savefig(dir + '/Graph_4-2_lesson_9', dpi=300)
plt.show()
