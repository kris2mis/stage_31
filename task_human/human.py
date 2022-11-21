# Необходимо реализовать программный компонент человека (human), у ко-
# торого обязательно должны быть следующие характеристики: имя (first
# name), фамилия (surname), возраст (age) и поле-состояние живой или нежи-
# вой (alive). Доступ к соответствующим полям организовать через соответ-
# ствующие свойства.
#
# В программном компоненте необходимо также реали-
# зовать поведение в виде метода, который определял бы, является ли чело-
# век совершеннолетним или нет, а также живой ли сейчас этот человек или
# его уже нет.
#
# Дополнительно у программного компонента должны быть реализованы конструктор и
# метод __str__(…) для представления состояния объекта в виде строки.
#
# Далее требуется написать небольшую программу, кото-
# рая бы создавала пару людей с различными параметрами и определяла
# сколько среди людей совершеннолетних, а сколько нет, а также выдавала
# статистику по живым и не живым.

# entity class
class Human:
    def __init__(self, first_name, surname, age=0, alive=True):
        self._first_name = first_name
        self._surname = surname
        self._age = age
        self._alive = alive

    def __str__(self):
        return (f"{self._first_name} {self._surname}: "
                f"age = {self._age},"
                f" is alive = {self._alive}")

    @property
    def firstname(self):
        return self._first_name

    @firstname.setter
    def firstname(self, firstname):
        self._first_name = firstname

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        self._surname = surname

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age > 0:
            self._age = age

    @property
    def alive(self):
        return self._alive

    @alive.setter
    def alive(self, alive):
        if alive > 0:
            self._alive = alive

    @property
    def is_adult(self):
        return self._age >= 18