students = {
    'alex' : 258,
    'max' : 227,
    'anna' : 278
}
print(students)
print(students['anna'])
print(students.get('alex'))
students['andrey'] = 268
print(students)
students['andrey'] = 177
print(students)
students.setdefault('oleg')  # Добавление элемента
print(students)
students.pop('oleg')  # Удаление элемента
print(students)
print(students.keys())  # Просмотр ключей
print(type(students.keys()))
key_list = list(students.keys())  # Преобразование в тип Список
print(key_list)
print(type(key_list))
print(students.values())  # Просмотр значений
print(type(students.values()))
print('anna' in students)  # Проверка существования ключа
print('peter' not in students)