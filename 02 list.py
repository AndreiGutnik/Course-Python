new_list = [1, 2, 3, 4]
mix_list = [12, 3.14, 'text']
print(len(new_list))  # Длина списка
print(new_list[0])  # Вывод значения по индексу
print(new_list[-1])
print(new_list[2:]) # Вывод всех значений, начиная с индексв

list_1 = ['anna', 'alex', 'max']
list_2 = ['john', 'nicolas', 'vlad']
print(list_1 + list_2) # Сложение спискоы
list_1[0] = 'artur'
print(list_1)
list_1.append('anna')  # Добавление элемента в конец списка
print(list_1)
list_1.insert(1, 'john')  # Добавление по указанному индексу
print(list_1)
print(list_1.index('max'))  # Отображение индекса по значению
list_1.index('max', 0, 10)  # Поиск значения между индексами
pop_del = list_1.pop()  # Удаление последнего значения спмска
print(pop_del)
print(list_1)
list_1.pop(0)  # Удаление значения по индексу
print(list_1)
list_1.clear()  # Очистка списка
print(list_1)

list_3 = ['33', '22', '11', '44']
print(list_3)
list_3.sort()  # Сортировка списка
print(list_3)
list_3.sort(reverse=True)  # Реверс списка с сортировкой
print(list_3)

list_4 = ['abcde', 'bcb', 'da', 'cde', 'ser', 'q']
print(list_4)
list_4.sort()
print(list_4)
list_4.sort(key=len)  # Сортировка по ключу
print(list_4)
list_4.reverse()  # Реверс списка
print(list_4)
