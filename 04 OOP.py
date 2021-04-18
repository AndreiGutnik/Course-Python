class CarsClass():
    """Класс автомобилей"""

    def __init__(self, brend, model, year, probeg):
        """Инициализация атрибутов"""
        self.brend = brend
        self.model = model
        self.year = year
        self.probeg = int(probeg)

    def showCar(self):
        """Показать информацию о машине"""
        print(f'{self.brend}, {self.model}, {self.year}, {self.probeg} km')

    def drowCar(self, km):
        """ Метод поездки авто """
        self.probeg = self.probeg + km


s_car = CarsClass('Lada', 'Granta', '2020', 10)
s_car.showCar()
s_car.drowCar(100)
s_car.showCar()


# ----------------НАСЛЕДОВАНИЕ--------------------
class ElectroCar(CarsClass):
    """Класс электрокаров, инициализация атрибутов"""

    def __init__(self, brand, model, year, probeg):
        super().__init__(brand, model, year, probeg)
        self.battery = 100  # потом удалить

    def description_battery(self):
        '''Выводит информацию о батарее'''
        print('Этот автомобиль имеет мощьность ' + str(self.battery) + ' %')

    def showCar(self):
        """Показать информацию о машине"""
        print(f'{self.brend}, {self.model}')


tesla = ElectroCar('Tesls', 'T', '2017', 10000)
tesla.showCar()
tesla.description_battery()
s_car.description_battery()
tesla.showCar()
s_car.showCar()

#
# class Battery():
#     """Класс батареи"""
#
#     def __init__(self, battery=100):
#         self.battery = battery
#
#     def description_battery(self):
#         '''Выводит информацию о батарее'''
#         print('Этот автомобиль имеет мощьность ' + str(self.battery) + ' %')
#
#
# class ElectroCar(CarsClass):
#     """Класс электрокаров"""
#
#     def __init__(self, brand, model, year, probeg):
#         super().__init__(brand, model, year, probeg)
#         self.battery = Battery()
#
#     def showCar(self):
#         """Показать информацию о машине"""
#         print(f'{self.brand}, {self.model}')
#
#
# akum = Battery()

# ----------------ИНКАПСУЛЯЦИЯ--------------------
'''
_ - перед свойством/методом означает защищенное свойство/метод
__ - перед свойством/методом означает приватное свойство/метод и к ним нет доступа извне
'''


class VkAccountInWebSite():
    """Ваш акккаунт в Vk, на сайте ВК"""

    def __init__(self, name, login_id, password):
        self.__name = name
        self.__login_id = login_id
        self.__password = password

    def publicLogin(self):
        self.__loginVk()

    def __loginVk(self):
        if self.__login_id == 123 and self.__password == 456:
            print('Привет ' + self.__name)
        return True


vkakk_1 = VkAccountInWebSite('Alex', 123, 456)
vkakk_1.loginVk()

# vkakk_1.name = 'Andrey'

print(vkakk_1.__name)

# ----------------МАГИЧЕСКИЕ МЕТОДЫ--------------------
'''
__repr__ - служит для вывода данных в log-файл 
__str__ - служит для вывода данных на сайт
'''


class New():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        # def __repr__(self):
        return self.name


new_obj = New('Иван')
print(new_obj)

# ----------------ИМПОРТ--------------------
'''
Для импорта данных из одного модуля в другой использоуется синтаксис:
from путь к файлу или имя файла без расширения import что импортируем (переменные, классы, функции и т.п.)

http://python.org Документация
https://pypi.org
'''
