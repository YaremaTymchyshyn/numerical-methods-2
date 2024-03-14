from math import *


def f(x):
    return tan(x) * tan(x) * tan(x)


def rectm(a, b, n):
    res = 0
    h = (b - a) / n
    x = a + (h / 2)
    for i in range(n):
        res += f(x)
        print('Iteration: ', res)
        x += h
    return h * res


print(rectm(1, 2, 10))
print('\n')


def trapm(a, b, n):
    res = 0
    h = (b - a) / n
    x = a
    for i in range(1, n):
        x += h
        res += f(x)
        print('Iteration: ', res)
    res *= 2
    res += f(a)
    res += f(b)
    return (h / 2) * res


print(trapm(1, 2, 10))
print('\n')


def parabm(a, b, n):
    h = (b - a) / n
    x = a
    res = f(x)
    res += f(b)
    for i in range(1, n):
        x += h
        temp = 2 * f(x) if i % 2 == 0 else 4 * f(x)
        print('Iteration: ', temp)
        res += temp
    return (h / 3) * res


print(parabm(1, 2, 10))
