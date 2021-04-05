print("Hello world!")
# Однострочный комментарий

'''
Многострочный 
комментарий
'''
print('Heloo world 2!')

# ТИПЫ ДАННЫХ
'''
int
1, 2, 3, -1, -2, -3

float
1.1, 3.14, 3.0

str
'Hello world!'

list
Список - это набор элементов
[1, 3.14, 'Hello']

dict
Словарь - это тип данных типа ключ-значение
{'alex':'123', 'anna':'321'}

tuple
Картежи - это немзменяемые списки
(1, 3.14, 'Hello')

set
Множество - это список из уникальных значений
{'a', 'b', 'c'}

bool
True
False

'''
# ПРЕОБРАЗОВАНИЕ ТИПОВ
x = 1
print(type(x))
x = float(x)
print(type(x))

# ПЕРЕМЕННЫЕ И МАТЕМАТИКА
'''
= знак равенства
== знак сравнения
+ - * / математические действия
Результат деления всегда float
round(float, 2)
% остаток от деления
** возведение в степень
'''

# ОПЕРАТОРЫ СРАВНЕНИЯ
'''
< > <= >= != ==
and or
True False
'''

# СТРОКИ str
'''
\ используется для экранирования
\\
r
\n перенос на новую строку
'''
text = str('hello world')
print(text)
print(text[0])  # элемент с индексом 0
print(text[0] + text[1])
print(text[-1] + text[1])  # Последний элемент
print(text[6:] + text[1])  # все элементы после 6
print(text[6:] + ' ' + text[:6])
print(text[6:8])  # символы между 6 и 9 индексами
print(text[::1])  # все элементы сшагом 1
print(text[::2])  # все элементы сшагом 2

# ФУНКЦИИ СТРОК
x = 'some long and awesome TEXT'
print(len(x))  # Длина строки
print(x[len(x) - 1])  # Последний символ
print(x[len(x) - 4:len(x)])  # Вывести 4 последних символа
print(x.count('o'))  # Количество вхождений элемента
print(x.find('a'))  # Индекс, где находится заданный символ
print(x.find('o'))
print(x.find('o'))
print(x.find('o', 3, 7))  # Диапазон с какого по какой индекс искать
print(x.find('o', 7))  # С какого индекса начинать поиск
print(x.find('and'))
print(x.find('TEXT'))
print(x.find('abc'))
print(x.capitalize())  # Преобразует строку, где первый символ в верхнем регистре
print(x.upper())  # Преобразование в верхний регистр
print(x.lower())  # Преобразование в нижний регистр
print('Old text: ' + x)
upper_cased = x.upper()
lower_cased = x.lower()
print(upper_cased.isupper())
print(lower_cased.islower())
print(x.isupper())  # Проверка находятся ли все символы в верхнем регистре
print(x.islower())  # Проверка находятся ли все символы в нижнем регистре

print('xxx777'.isalnum())  # Проверка состоит ли строка только из букв и цифр
print('xxx777!'.isalnum())
print('xxx777'.isalpha())  # Проверка состоит ли строка только из букв
print('xxx'.isalpha())
print('   '.isspace())  # Проверка наличия пробела
print(''.isspace())
empty_string = ''
print(empty_string == '')  # true
print(empty_string == ' ')  # false
print(empty_string.strip(' ') == '')  # true Удаление символа
empty_string = ' '
print(empty_string.strip() == '')

empty_string = ''
if not empty_string:
    print('not empty')
else:
    print('empty')

x = str('hello')
print(x.startswith('he'))  # Проверка начинается ли строка с символов
print(x.endswith('lo'))  # Проверка заканчивается ли строка символами
split = x.split('l')  # Разбивает строку на части, используя разделитель
print(type(split))
print(split)
split = x.split('e')
print(split)
some_data = '4;8;15;16;23;42'
separated_data = some_data.split(';')
print(separated_data)
print(separated_data[3])

# ФОРМАТИРОВАНИЕ СТРОК
x = '10'
y = 'cold'
print('Weather: temperature +{} and it\'s {}'.format(x, y))
print('Weather: temperature +{1} and it\'s {0}'.format(x, y))
print(f'Weather: temperature +{x} and it\'s {y}')
pi = 3.141532
print(pi)
print(f'pi equals {pi:0.2f}')
print(f'pi equals {pi:0.5f}')
