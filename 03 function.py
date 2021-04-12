def sqRing(r):
    s = 3.1415 * (r ** 2)
    print(s)


# return s

sqRing(33)
sqRing(70)


# --------------Функция с параметрами по-умолчанию------------------------------

def printText(msg, end='!'):
    print(msg + end)


printText('Text')
printText('Text', '?')


# --------------Определение функции с описанием------------------------------

def function(a, b, c):
    """
    :param a: Описание1
    :param b: Описание2
    :param c: Описание3
    :return: Описание4
    """
    return a + b + c


help(function)

# -----------Распаковка элементов---------------------------------

# a, b, c = 10, 20, 30
a, *b, c = 'Строка', 10, 20, 3.14, 10, 'Текст', 11, 22, 34

print(a)
print(b)
print(c)

s = [4, 10]
print(list(range(1, 6)))
print(list(range(*s)))


def func(a, b, c, d):
    print(a, b, c, d)


a = ('hello', True, 78, [3, 4, 5])
func(*a)

'''
Функции args и kwargs служат для упаковки неограниченного количества значений в
картеж или словарь и передавать их в функцию
'''


def func(*args):
    print(sum(args) * 0.06)


func(1, 33, 11444, 1111, 4444, )
func(1, 33, 11444, 1111, 4444, 1000, 4434, 4444, 6666)


def func(**kwargs):
    print(kwargs)


func(a=1, b=2, c=3)


def func(*args, **kwargs):
    print(args)
    print(kwargs)


func(1, 2, 3, 4, 5, a=1, b=2, c=3)


# -------------------Преобразование итерируемых объектов-------------------------

# map(func, iterable) Применение функции для всех элементов итерабельного объекта
def sq(x):
    return x ** 2


a = [-2, -1, 5, 7, 3]

b = map(sq, a)
print(b)

c = list(map(sq, a))

print(c)

'''
Применение функции (только с булевым результатом) для всех элементов итерабельного объекта,
исключая результаты, которые не являются True
'''


def is_adult(age):
    return age >= 18


age = [11, 20, 18, 33, 14, 12]

print(filter(is_adult, age))
print(list(filter(is_adult, age)))

# lambda - это формат записания функции без ее объявления
age = [11, 20, 18, 33, 14, 12]

print(list(filter(lambda age: age >= 18, age)))


# -----------------ДЕКОРАТОРЫ---------------------------

#  Это функция, которая в качестве аргумента принимает другую функцию и расширяет ее функционал
def tagMaker(func):
    def wrapper(*args, **kwargs):
        print('<div>')
        func(*args, **kwargs)
        print('</div>')

    return wrapper


# @tagMaker
def printText(text):
    print(text)


printText('Hello World')

import time
import datetime


def recTime(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        func(*args, **kwargs)
        bone = datetime.datetime.now() - start
        print(f'Функция завершилась за {bone} сек')

    return wrapper


@recTime
def sfunc():
    time.sleep(3)
    print('Завершено!')


sfunc()

# -----------------ОШИБКИ И ИСКЛЮЧЕНИЯ---------------------------
import requests
import time
from datetime import datetime

while True:
    try:
        a = requests.get('https://yandex.ru')
        print(a)
        time.sleep(60)
        if a == '<Response [200]>':
            pass
        elif a == '<Response [503]>':
            print('ошибка сайта')
        else:
            print('иная ошибка')
    except requests.exceptions.ConnectionError:
        error_time = datetime.now()
        print('Сервер упал!\n' + str(error_time))
    #except Exception as e:
    #    print(e, type(e))
    finally:
        print('Завершено!')
