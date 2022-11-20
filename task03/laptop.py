# Необходимо реализовать программный компонент, эмулирующий компью-
# тер (computer) или ноутбук (laptop).
#
# Минимум программный компонент дол-
# жен содержать следующие параметры: бренд (brand), модель (model) и цену
# (price).
#
# Остальные параметры можно выбрать самостоятельно исходя из бу-
# дущей логики программной системы. Доступ к соответствующим полям ор-
# ганизовать через соответствующие свойства.
#
# Также у программного компонента должны быть реализованы
# конструктор и метод __str__(…) для пред-
# ставления состояния объекта в виде строки.
#
# Далее требуется написать не-
# большую программу, которая бы создавала пару компьютеров с различ-
# ными параметрами и определяла общую стоимость всех компьютеров, а
# также находила самый дорогой и дешёвый компьютеры.

# entity class
class Laptop:
    def __init__(self, brand, model, price):
        self._brand = brand
        self._model = model
        self._price = price

    def __str__(self):
        return (f"{self._brand} {self._model}. "
                f"\nPrice: {self._price}$")

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price > 0:
            self._price = price
