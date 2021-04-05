# Множество - это список из уникальных значений
first_set = {'Alex', 'John', 'Georg', 'Alex'}
print(type(first_set))
print(first_set)
print(len(first_set))
first_set.add('Maxim')  # Добавление элемента
print(first_set)
print('Maxim' in first_set)  # Проверка наличия элемента
first_set.remove('Alex')  # Удаление элемента
print(first_set)
first_set.clear()  # Очистка множества
print(first_set)

first_set = {'Alex', 'John', 'Georg', 'Alex'}
second_set = {'Anton', 'Tom', 'Anna', 'Alex'}
third_set = first_set.union(second_set)  # Объединение множеств
print(third_set)
fourth_set = first_set.intersection(second_set)  # Пересечение множеств
print(fourth_set)
fifth_set = first_set.difference(second_set)  # Присутствуют в первом, но отсутствуют во втором
print(fifth_set)
print(fifth_set - second_set)  # Вычитание

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(set1.issubset(set2))  # Проверка содержания значений первого множества во втором
print(set2.issuperset(set1))  #  И наоборот
# print(set1[0]) НЕ ПОДДЕРЖИВАЕТ ОБРАЩЕНИЕ ПО ИНДЕКСУ

f_list = list(first_set)
print(f_list)